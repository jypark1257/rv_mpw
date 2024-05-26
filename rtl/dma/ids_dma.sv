
module ids_dma #(
    parameter PIM_CTRL          = 32'h2000_0010,
    parameter PIM_R             = 32'h2000_0020,
    parameter PIM_W_WEIGHT      = 32'h2000_0040,
    parameter PIM_W_ACTIVATION  = 32'h2000_0080
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
    input           [11:0]  i_size,       // maximum available transfer count: 8192 (32K * byte)
    input           [31:0]  i_mem_addr,
    // bus request 
    output  logic           o_bus_req,
    input                   i_bus_gnt,
    // bus interface
    output  logic   [31:0]  o_dma_addr,
    output  logic           o_dma_write,
    output  logic           o_dma_read,
    output  logic   [3:0]   o_dma_size,
    output  logic   [31:0]  o_dma_wr_data,
    input           [31:0]  i_dma_rd_data,
    // DMA status
    output  logic           o_dma_busy
);

    localparam IDLE     = 3'b000;
    localparam RW_SETUP = 3'b001;  
    localparam R_EXE    = 3'b010;  
    localparam W_EXE    = 3'b011;   

    localparam FUNCT_WEIGHT = 2'b01;
    localparam FUNCT_ACT    = 2'b10;
    
    localparam PIM_WRITE    = 3'b001;    // write weight to pim
    localparam PIM_COMPUTE  = 3'b010;    // write activation to pim
    localparam PIM_LOAD     = 3'b100;   // load output result from pim

    // PIM status
    logic pim_busy;
    logic pim_data_valid; 

    // request for operation?
    logic operation_start;

    // operand fetch
    logic [2:0] funct3;
    logic [3:0] sel_pim;
    logic [11:0] size;
    logic [31:0] mem_addr;

    // current state, next state
    logic [2:0] curr_state;
    logic [2:0] next_state;

    // counter
    logic [12:0] trans_counter;     // maximum available transfer count: 8192 (32K * byte)
    logic count_start;
    logic [12:0] data_count;   // GENERATE FROM FSM
    logic trans_running;

    // control signals
    logic mem_incr;
    logic rw_edge;
    
    // PIM address
    logic [31:0] pim_write_addr;
    
    // --|PIM status|--------------------------------------------------------------------
    // transfer data when       (!pim_busy)
    // load data from pim when  (!pim_busy) && (pim_data_valid) 
    assign pim_busy = i_dma_rd_data[0];
    assign pim_data_valid = i_dma_rd_data[1];

    // --|PIM address select|-------------------------------------------------------------
    always_comb begin
        case (funct3)
            3'b001: pim_write_addr = PIM_W_WEIGHT | sel_pim;
            3'b010: pim_write_addr = PIM_W_ACTIVATION | sel_pim;
            default: pim_write_addr = '0;
        endcase
    end


    // --|operand fetch|------------------------------------------------------------------
    assign operation_start = i_dma_en && (!trans_running);

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
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
        if (~i_rst_n) begin
            trans_counter <= '0;
        end else begin
            if (count_start) begin
                trans_counter <= data_count;
            end else if (rw_edge && trans_running) begin    // while running
                trans_counter <= trans_counter - 1;
            end
        end
    end    

    // --|FSM|------------------------------------------------------------
    // state transition
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
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
                    if ((funct3 == PIM_WRITE) || (funct3 == PIM_COMPUTE)) begin
                        if (!pim_busy) begin
                            next_state = R_EXE;
                        end else begin
                            next_state = RW_SETUP;
                        end
                    end else if (funct3 == PIM_LOAD) begin
                        if ((!pim_busy) && pim_data_valid) begin
                            next_state = R_EXE;
                        end else begin
                            next_state = RW_SETUP;
                        end
                    end else begin
                    
                    end
                end else begin
                    next_state = RW_SETUP;
                end
            end
            R_EXE: begin
                if (!i_bus_gnt) begin
                    next_state = R_EXE;
                end else begin      // bus_gnt && trans_running
                    next_state = W_EXE;
                end
            end
            W_EXE: begin
                if (!trans_running) begin   // go to IDLE when transfer is done
                    next_state = IDLE;
                end else if (!i_bus_gnt) begin
                    next_state = W_EXE;
                end else begin      // bus_gnt
                    next_state = R_EXE;
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
        mem_incr = '0;
        o_dma_addr = '0;
        o_dma_write = '0;
        o_dma_read = '0;
        o_dma_size = '0;
        o_dma_wr_data = '0;
        rw_edge = '0;
        case (curr_state)
            RW_SETUP: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                count_start = 1'b1;
                // read PIM control signal
                o_dma_addr = PIM_CTRL;
                o_dma_write = 1'b0;
                o_dma_read = 1'b1;
                o_dma_size = 4'b1111;
                o_dma_wr_data = '0;
            end
            R_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin
                    o_dma_addr = ((funct3 == PIM_WRITE) || (funct3 == PIM_COMPUTE)) ? mem_addr : PIM_R;
                    o_dma_write = 1'b0;
                    o_dma_read = 1'b1;
                    o_dma_size = 4'b1111;
                    o_dma_wr_data = '0;
                    rw_edge = 1'b1;
                end else begin
                    o_dma_addr = '0;
                    o_dma_write = 1'b0;
                    o_dma_read = 1'b0;
                    o_dma_size = 4'b0000;
                    o_dma_wr_data = '0;
                end
            end
            W_EXE: begin
                o_dma_busy = 1'b1;
                o_bus_req = 1'b1;
                if (i_bus_gnt) begin
                    mem_incr = 1'b1;
                    o_dma_addr = (funct3 == PIM_LOAD) ? mem_addr : pim_write_addr;
                    o_dma_write = 1'b1;
                    o_dma_read = 1'b0;
                    o_dma_size = 4'b1111;
                    o_dma_wr_data = i_dma_rd_data;
                end else begin
                    o_dma_addr = '0;
                    o_dma_write = 1'b0;
                    o_dma_read = 1'b0;
                    o_dma_size = 4'b0000;
                    o_dma_wr_data = '0;
                end
            end
            default: begin
                o_dma_busy = '0;
                o_bus_req = '0;
                count_start = '0;
                mem_incr = '0;
                o_dma_addr = '0;
                o_dma_write = '0;
                o_dma_read = '0;
                o_dma_size = '0;
                o_dma_wr_data = '0;
                rw_edge = '0;
            end
        endcase
    end


endmodule