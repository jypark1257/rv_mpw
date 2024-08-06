
module pim_dma #(
    parameter PIM_CTRL          = 32'h4000_0010,
    parameter PIM_R             = 32'h4000_0020,
    parameter PIM_W_WEIGHT      = 32'h4000_0040,
    parameter PIM_W_ACTIVATION  = 32'h4000_0080,
    parameter PIM_W_KEY         = 32'h4000_0100,
    parameter PIM_W_VREF        = 32'h4000_0200
) (
    input                   i_clk,
    input                   i_rst_n,
    // DMA enable
    input                   i_dma_en,
    // pim instruction
    // 3'b001: pim_write
    // 3'b010: pim_compute
    // 3'b100: pim_load
    input           [2:0]   i_funct3,
    input           [3:0]   i_sel_pim,
    input           [12:0]  i_size,       // maximum available transfer count: 8192 (32K * byte)
    input           [31:0]  i_mem_addr,
    // bus request 
    output  logic           o_bus_req,
    input                   i_bus_gnt,
    // bus interface (SRAM)
    output  logic   [31:0]  o_dma_addr_0,
    output  logic           o_dma_write_0,
    output  logic           o_dma_read_0,
    output  logic   [3:0]   o_dma_size_0,
    output  logic   [31:0]  o_dma_wr_data_0,
    input           [31:0]  i_dma_rd_data_0,
    // bus interface (PIM)
    output  logic   [31:0]  o_dma_addr_1,
    output  logic           o_dma_write_1,
    output  logic           o_dma_read_1,
    output  logic   [3:0]   o_dma_size_1,
    output  logic   [31:0]  o_dma_wr_data_1,
    input           [31:0]  i_dma_rd_data_1,
    // DMA status
    output  logic           o_dma_busy
);

    // FSM states
    typedef enum logic [2:0] { IDLE, RW_SETUP, R_EXE, RW_EXE, R_PIM_EXE, RW_PIM_EXE } e_state;

    localparam FUNCT_WEIGHT = 2'b01;
    localparam FUNCT_ACT    = 2'b10;

    localparam PIM_WRITE    = 3'b001;   // write weight to pim
    localparam PIM_COMPUTE  = 3'b010;   // write activation to pim
    localparam PIM_LOAD     = 3'b100;   // load output result from pim
    localparam PIM_KEY    = 3'b101;   // write keys
    localparam PIM_VREF   = 3'b110;

    // PIM status
    logic pim_busy;
    logic pim_data_valid; 

    // request for operation?
    logic operation_start;

    // operand fetch
    logic [2:0] funct3;
    logic [3:0] sel_pim;
    logic [12:0] size;
    logic [31:0] mem_addr;

    // current state, next state
    e_state curr_state;
    e_state next_state;

    // counter
    logic [13:0] trans_counter;     // maximum available transfer count: 8192 (32K * byte)
    logic count_start;
    logic [13:0] data_count;   // GENERATE FROM FSM
    logic trans_running;

    // control signals
    logic mem_incr;
    logic cnt_decr;
    
    // PIM address
    logic [31:0] pim_write_addr;
    logic [31:0] pim_read_addr;
    
    // --|PIM status|--------------------------------------------------------------------
    // transfer data when       (!pim_busy)
    // load data from pim when  (!pim_busy) && (pim_data_valid) 
    assign pim_busy = i_dma_rd_data_1[0];
    assign pim_data_valid = i_dma_rd_data_1[1];

    // --|PIM address select|-------------------------------------------------------------
    always_comb begin
        case (funct3)
            PIM_WRITE: pim_write_addr = PIM_W_WEIGHT | sel_pim;
            PIM_COMPUTE: pim_write_addr = PIM_W_ACTIVATION | sel_pim;
            PIM_LOAD: pim_read_addr = PIM_R | sel_pim;
            PIM_KEY: pim_write_addr = PIM_W_KEY | sel_pim;
            PIM_VREF: pim_write_addr = PIM_W_VREF | sel_pim;
            default: begin
                pim_write_addr = '0;
                pim_read_addr = '0;
            end
        endcase
    end

    // --|operand fetch|------------------------------------------------------------------
    assign operation_start = i_dma_en && (!trans_running);

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            funct3 <= '0;
            sel_pim <= '0;
            size <= '0;
            mem_addr <= '0;
        end else begin
            if (operation_start) begin
                funct3 <= i_funct3;
                sel_pim <= i_sel_pim;
                size <= i_size;
                mem_addr <= i_mem_addr;
            end else begin
                funct3 <= funct3;
                sel_pim <= sel_pim;
                size <= size;
                // mem address increment
                if (mem_incr) begin
                    mem_addr <= mem_addr + 4;
                end else begin
                    mem_addr <= mem_addr;
                end
            end
        end
    end


    // --|counter|-----------------------------------------------------------
    assign trans_running = trans_counter != '0;
    assign data_count = size;
    
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            trans_counter <= '0;
        end else begin
            if (count_start) begin
                trans_counter <= data_count;
            end else if (cnt_decr && trans_running) begin    // while running
                trans_counter <= trans_counter - 1;
            end
        end
    end    

    // --|FSM|------------------------------------------------------------
    // state transition
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            curr_state <= IDLE;
        end else begin
            curr_state <= next_state;        
        end
    end

    // next state logic
    always_comb begin
        case (curr_state)
            IDLE: begin
                if (operation_start) begin
                    next_state = RW_SETUP;
                end else begin
                    next_state = IDLE;
                end
            end
            RW_SETUP: begin
                if (i_bus_gnt) begin
                    if ((funct3 == PIM_WRITE) || (funct3 == PIM_COMPUTE) || (funct3 == PIM_KEY) || (funct3 == PIM_VREF)) begin
                        if (!pim_busy) begin
                            next_state = R_EXE;
                        end else begin
                            next_state = RW_SETUP;
                        end
                    end else if (funct3 == PIM_LOAD) begin
                        if ((!pim_busy) && pim_data_valid) begin
                            next_state = R_PIM_EXE;
                        end else begin
                            next_state = RW_SETUP;
                        end
                    end else begin
                        next_state = RW_SETUP;
                    end
                end else begin
                    next_state = RW_SETUP;
                end
            end
            R_PIM_EXE: begin
                if (!i_bus_gnt) begin
                    next_state = R_PIM_EXE;
                end else begin
                    next_state = RW_PIM_EXE;
                end
            end
            R_EXE: begin
                if (!i_bus_gnt) begin
                    next_state = R_EXE;
                end else begin      // bus_gnt && trans_running
                    next_state = RW_EXE;
                end
            end
            RW_EXE: begin
                if (!trans_running) begin   // go to W_EXE when transfer is done
                    next_state = IDLE;
                end else if (!i_bus_gnt) begin
                    next_state = RW_EXE;
                end else begin              // bus_gnt
                    next_state = RW_EXE;
                end
            end
            RW_PIM_EXE: begin
                if (!trans_running) begin   // go to W_EXE when transfer is done
                    next_state = IDLE;
                end else if (!i_bus_gnt) begin
                    next_state = RW_PIM_EXE;
                end else begin              // bus_gnt
                    next_state = RW_PIM_EXE;
                end
            end
            default: begin
                next_state = IDLE;
            end
        endcase
    end 
    
    // output logic
    always_comb begin
        o_dma_busy = '0;
        o_bus_req = '0;
        count_start = '0;
        cnt_decr = '0;
        mem_incr = '0;
        // DMA SRAM I/F
        o_dma_addr_0 = '0;
        o_dma_write_0 = '0;
        o_dma_read_0 = '0;
        o_dma_size_0 = '0;
        o_dma_wr_data_0 = '0;
        // DMA PIM I/F
        o_dma_addr_1 = '0;
        o_dma_write_1 = '0;
        o_dma_read_1 = '0;
        o_dma_size_1 = '0;
        o_dma_wr_data_1 = '0;
        case (curr_state)
            RW_SETUP: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                count_start = 1'b1;
                // read PIM control signal
                o_dma_addr_1 = PIM_CTRL;
                o_dma_write_1 = '0;
                o_dma_read_1 = 1'b1;
                o_dma_size_1 = 4'b1111;
                o_dma_wr_data_1 = '0;
            end
            R_PIM_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin
                    cnt_decr = 1'b1;
                    mem_incr = 1'b0;
                    // DMA SRAM I/F
                    o_dma_addr_0 = '0;
                    o_dma_write_0 = '0;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = 4'b1111;
                    o_dma_wr_data_0 = '0;

                    o_dma_addr_1 = pim_read_addr;
                    o_dma_write_1 = 1'b0;
                    o_dma_read_1 = 1'b1;
                    o_dma_size_1 = 4'b1111;
                    o_dma_wr_data_1 = '0;
                end else begin
                    cnt_decr = '0;    
                    mem_incr = '0;         
                    o_dma_addr_0 = '0;
                    o_dma_write_0 = '0;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = '0;
                    o_dma_wr_data_0 = '0;

                    o_dma_addr_1 = '0;
                    o_dma_write_1 = '0;
                    o_dma_read_1 = '0;
                    o_dma_size_1 = '0;
                    o_dma_wr_data_1 = '0;
                end
            end
            R_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin
                    cnt_decr = 1'b1;
                    mem_incr = 1'b1;
                    // DMA SRAM I/F
                    o_dma_addr_0 = mem_addr;
                    o_dma_write_0 = 1'b0;
                    o_dma_read_0 = 1'b1;
                    o_dma_size_0 = 4'b1111;
                    o_dma_wr_data_0 = '0;

                    o_dma_addr_1 = '0;
                    o_dma_write_1 = '0;
                    o_dma_read_1 = '0;
                    o_dma_size_1 = 4'b1111;
                    o_dma_wr_data_1 = '0;
                end else begin
                    cnt_decr = '0;    
                    mem_incr = '0;         
                    o_dma_addr_0 = '0;
                    o_dma_write_0 = '0;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = '0;
                    o_dma_wr_data_0 = '0;

                    o_dma_addr_1 = '0;
                    o_dma_write_1 = '0;
                    o_dma_read_1 = '0;
                    o_dma_size_1 = '0;
                    o_dma_wr_data_1 = '0;
                end
            end
            RW_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin   
                    cnt_decr = 1'b1;    
                    mem_incr = 1'b1;             
                    // DMA SRAM I/F
                    //o_dma_addr_0 = ((funct3 == PIM_WRITE) || (funct3 == PIM_COMPUTE)) ? mem_addr : pim_read_addr;
                    o_dma_addr_0 = (!trans_running) ? '0 : mem_addr;
                    o_dma_write_0 = 1'b0;
                    o_dma_read_0 = (!trans_running) ? 1'b0 : 1'b1;
                    o_dma_size_0 = 4'b1111;
                    o_dma_wr_data_0 = '0;
            
                    o_dma_addr_1 = pim_write_addr;
                    o_dma_write_1 = 1'b1;
                    o_dma_read_1 = 1'b0;
                    o_dma_size_1 = 4'b1111;
                    o_dma_wr_data_1 = i_dma_rd_data_0;
                end else begin
                    cnt_decr = '0;    
                    mem_incr = '0;         
                    o_dma_addr_0 = '0;
                    o_dma_write_0 = '0;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = '0;
                    o_dma_wr_data_0 = '0;
                    o_dma_addr_1 = '0;
                    o_dma_write_1 = '0;
                    o_dma_read_1 = '0;
                    o_dma_size_1 = '0;
                    o_dma_wr_data_1 = '0;
                end
            end
            RW_PIM_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin   
                    cnt_decr = 1'b1;    
                    mem_incr = 1'b1;             
                    // DMA SRAM I/F
                    //o_dma_addr_0 = ((funct3 == PIM_WRITE) || (funct3 == PIM_COMPUTE)) ? mem_addr : pim_read_addr;
                    o_dma_addr_0 = mem_addr;
                    o_dma_write_0 = 1'b1;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = 4'b1111;
                    o_dma_wr_data_0 = i_dma_rd_data_1;
        
                    o_dma_addr_1 = (!trans_running) ? '0 : pim_read_addr;
                    o_dma_write_1 = 1'b0;
                    o_dma_read_1 = (!trans_running) ? 1'b0 : 1'b1;
                    o_dma_size_1 = 4'b1111;
                    o_dma_wr_data_1 = '0;
                end else begin
                    cnt_decr = '0;    
                    mem_incr = '0;         
                    o_dma_addr_0 = '0;
                    o_dma_write_0 = '0;
                    o_dma_read_0 = '0;
                    o_dma_size_0 = '0;
                    o_dma_wr_data_0 = '0;
                    o_dma_addr_1 = '0;
                    o_dma_write_1 = '0;
                    o_dma_read_1 = '0;
                    o_dma_size_1 = '0;
                    o_dma_wr_data_1 = '0;
                end
            end
            default: begin
                o_dma_busy = '0;
                o_bus_req = '0;
                count_start = '0;
                mem_incr = '0;
                cnt_decr = '0;
                o_dma_addr_0 = '0;
                o_dma_write_0 = '0;
                o_dma_read_0 = '0;
                o_dma_size_0 = '0;
                o_dma_wr_data_0 = '0;
                o_dma_addr_1 = '0;
                o_dma_write_1 = '0;
                o_dma_read_1 = '0;
                o_dma_size_1 = '0;
                o_dma_wr_data_1 = '0;
            end
        endcase
    end
endmodule