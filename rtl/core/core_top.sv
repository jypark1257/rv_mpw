module core_top #(
    parameter XLEN = 32,
    parameter CPU_CLOCK_FREQ = 100_000_000,
    parameter RESET_PC = 32'h4000_0000,
    parameter BAUD_RATE = 115200
) (
    input                   i_clk,
    input                   i_rst_n,

    input                   i_serial_rx,
    output logic            o_serial_tx
);

    logic [XLEN-1:0]        data_addr_q;

    // RV IMEM I/F
    logic [XLEN-1:0]        instr_addr;
    logic [XLEN-1:0]        instr_rd_data;
    logic [XLEN-1:0]        instr_wr_data;
    logic [3:0]             instr_size;
    logic                   instr_read;
    logic                   instr_write;

    // RV DMEM I/F
    logic                   req_dmem;
    logic                   gnt_dmem;
    logic [XLEN-1:0]        data_addr;
    logic [XLEN-1:0]        data_rd_data;
    logic [XLEN-1:0]        data_wr_data;
    logic [3:0]             data_size;
    logic                   data_read;
    logic                   data_write;

    // SRAM IMEM I/F
    logic [XLEN-1:0]        imem_addr;
    logic [XLEN-1:0]        imem_rd_data;
    logic [XLEN-1:0]        imem_wr_data;
    logic [3:0]             imem_size;
    logic                   imem_read;
    logic                   imem_write;

    // SRAM DMEM I/F
    logic [XLEN-1:0]        dmem_addr;
    logic [XLEN-1:0]        dmem_rd_data;
    logic [XLEN-1:0]        dmem_wr_data;
    logic [3:0]             dmem_size;  
    logic                   dmem_read;
    logic                   dmem_write;
    // Select between DMA and BUS signal
    logic [XLEN-1:0]        rd_data;

    
    // UART
    logic [XLEN-1:0]        uart_addr;
    logic [XLEN-1:0]        uart_rd_data;
    logic [XLEN-1:0]        uart_wr_data;
    logic [3:0]             uart_size;  
    logic                   uart_read;
    logic                   uart_write;

    // DMA
    logic                   dma_en;
    logic [2:0]             dma_funct3;
    logic [3:0]             dma_sel_pim;
    logic [11:0]            dma_trans_size;
    logic [XLEN-1:0]        dma_mem_addr;
    logic                   req_dma;
    logic                   gnt_dma;
    logic [XLEN-1:0]        dma_addr;
    logic                   dma_write;
    logic                   dma_read;
    logic [3:0]             dma_size;  
    logic [XLEN-1:0]        dma_rd_data;
    logic [XLEN-1:0]        dma_wr_data;
    logic                   dma_busy;
    

    core #(
        .RESET_PC           (RESET_PC)
    ) core_0 (
        .i_clk              (i_clk),
        .i_rst_n            (i_rst_n),

        // instruction interface
        .o_instr_addr       (instr_addr),
        .i_instr_rd_data    (instr_rd_data),
        .o_instr_wr_data    (instr_wr_data),
        .o_instr_size       (instr_size),
        .o_instr_read       (instr_read),
        .o_instr_write      (instr_write),

        // data interface
        .o_req_dmem         (req_dmem),
        .i_gnt_dmem         (gnt_dmem),
        .o_data_addr        (data_addr),
        .i_data_rd_data     (rd_data),
        .o_data_wr_data     (data_wr_data),
        .o_data_size        (data_size),
        .o_data_read        (data_read),
        .o_data_write       (data_write),

        .o_dma_en           (dma_en),
        .o_dma_funct3       (dma_funct3),
        .o_dma_sel_pim      (dma_sel_pim),
        .o_dma_size         (dma_trans_size),
        .o_dma_mem_addr     (dma_mem_addr)
    );

    ids_dma #(
        .PIM_CTRL           (32'h2000_0010),
        .PIM_R              (32'h2000_0020),
        .PIM_W_WEIGHT       (32'h2000_0040),
        .PIM_W_ACTIVATION   (32'h2000_0080)
    ) dma_0 (
        .i_clk              (i_clk),
        .i_rst_n            (i_rst_n),
        // CORE interface
        .i_dma_en           (dma_en),
        .i_funct3           (dma_funct3),
        .i_sel_pim          (dma_sel_pim),
        .i_size             (dma_trans_size),      
        .i_mem_addr         (dma_mem_addr),
        // BUS interface
        .o_bus_req          (req_dma),
        .i_bus_gnt          (gnt_dma),
        .o_dma_addr         (dma_addr),
        .o_dma_write        (dma_write),
        .o_dma_read         (dma_read),
        .o_dma_size         (dma_size),
        .o_dma_wr_data      (dma_wr_data),
        .i_dma_rd_data      (dma_rd_data),
        // busy signal
        .o_dma_busy         (dma_busy)
    );


    // DMA control signal read
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
            data_addr_q <= '0;
        end else begin
            data_addr_q <= (data_read) ? data_addr : '0;
        end
    end
        
    assign rd_data = (data_addr_q == 32'h1000_0000) ? {31'h0, 1'b0} : data_rd_data;  


    // IDS BUS
    ids_bus bus_0 (
        .i_clk              (i_clk), 
        .i_rst_n            (i_rst_n),

    // RV IMEM
        .i_imem_addr        (instr_addr),
        .i_imem_write       (instr_write),
        .i_imem_read        (instr_read),
        .i_imem_size        (instr_size),
        .i_imem_din         (instr_wr_data),
        .o_imem_dout        (instr_rd_data),

    // RV DMEM
        .i_req_dmem         (req_dmem),
        .o_gnt_dmem         (gnt_dmem),
        .i_dmem_addr        (data_addr),
        .i_dmem_write       (data_write),
        .i_dmem_read        (data_read),
        .i_dmem_size        (data_size),
        .i_dmem_din         (data_wr_data),
        .o_dmem_dout        (data_rd_data),

    // DMA
        .i_req_dma          (req_dma),
        .o_gnt_dma          (gnt_dma),
        .i_dma_addr         (dma_addr),
        .i_dma_write        (dma_write),
        .i_dma_read         (dma_read),
        .i_dma_size         (dma_size),
        .i_dma_din          (dma_wr_data),
        .o_dma_dout         (dma_rd_data),

    // IMEM SRAM (IMEM port)
        .o_imem_addr        (imem_addr),
        .o_imem_write       (imem_write),
        .o_imem_read        (imem_read),
        .o_imem_size        (imem_size),
        .o_imem_din         (imem_wr_data),
        .i_imem_dout        (imem_rd_data),

    // DMEM SRAM (DMEM port)
        .o_dmem_addr        (dmem_addr),
        .o_dmem_write       (dmem_write),
        .o_dmem_read        (dmem_read),
        .o_dmem_size        (dmem_size),
        .o_dmem_din         (dmem_wr_data),
        .i_dmem_dout        (dmem_rd_data),   
        // UART
        .o_uart_addr        (uart_addr),
        .o_uart_write       (uart_write),
        .o_uart_read        (uart_read),
        .o_uart_size        (uart_size),
        .o_uart_din         (uart_wr_data),
        .i_uart_dout        (uart_rd_data)

    );

    // IMEM
    imem #(
        .MEM_DEPTH          (4096),
        .MEM_ADDR_WIDTH     (12)
    ) imem_0 (
        .i_clk              (i_clk),

        .i_instr_addr       (imem_addr),
        .o_instr_rd_data    (imem_rd_data),
        .i_instr_wr_data    (imem_wr_data),
        .i_instr_size       (imem_size),
        .i_instr_write      (imem_write),
        .i_instr_read       (imem_read)
    );

    // DMEM
    dmem #(
        .MEM_DEPTH          (4096),
        .MEM_ADDR_WIDTH     (12)
    ) dmem_0 (
        .i_clk              (i_clk),

        .i_data_addr        (dmem_addr),
        .o_data_rd_data     (dmem_rd_data),
        .i_data_wr_data     (dmem_wr_data),
        .i_data_size        (dmem_size),
        .i_data_write       (dmem_write),
        .i_data_read        (dmem_read)
    );

    uart_wrap #(
        .CLOCK_FREQ         (CPU_CLOCK_FREQ),
        .BAUD_RATE          (BAUD_RATE)
    ) on_chip_uart (
        .i_clk              (i_clk), 
        .i_rst_n            (i_rst_n), 
        .i_uart_addr        (uart_addr),
        .i_uart_write       (uart_write),
        .i_uart_read        (uart_read),
        .i_uart_size        (uart_size),
        .i_uart_din         (uart_wr_data),
        .o_uart_dout        (uart_rd_data),
        .i_serial_rx        (i_serial_rx),
        .o_serial_tx        (o_serial_tx)
    );


endmodule