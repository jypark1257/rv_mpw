module core_top #(
    parameter XLEN = 32,
    parameter CPU_CLOCK_FREQ = 100_000_000,
    parameter RESET_PC = 32'h4000_0000,
    parameter BAUD_RATE = 115200
) (
    input i_clk,
    input i_rst_n,

    input i_serial_rx,
    output logic o_serial_tx
);

    logic [XLEN-1:0]    instr_addr_q;
    logic [XLEN-1:0]    data_addr_q;

    // RV IMEM I/F
    logic [XLEN-1:0]    instr_addr;
    logic [XLEN-1:0]    instr_rd_data;
    logic [XLEN-1:0]    instr_wr_data;
    logic [3:0]         instr_size;
    logic               instr_read;
    logic               instr_write;

    // RV DMEM I/F
    logic               req_dmem;
    logic               gnt_dmem;
    logic [XLEN-1:0]    data_addr;
    logic [XLEN-1:0]    data_rd_data;
    logic [XLEN-1:0]    data_wr_data;
    logic [3:0]         data_size;
    logic               data_read;
    logic               data_write;

    // SRAM IMEM I/F
    logic [XLEN-1:0]    imem_addr;
    logic [XLEN-1:0]    imem_rd_data;
    logic [XLEN-1:0]    imem_wr_data;
    logic [3:0]         imem_size;
    logic               imem_read;
    logic               imem_write;

    // SRAM DMEM I/F
    logic [XLEN-1:0]    dmem_addr;
    logic [XLEN-1:0]    dmem_rd_data;
    logic [XLEN-1:0]    dmem_wr_data;
    logic [3:0]         dmem_size;  
    logic               dmem_read;
    logic               dmem_write;
    
    // UART
    logic [7:0] data_in;
    logic [7:0] data_out;
    

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
        .o_instr_read        (instr_read),
        .o_instr_write       (instr_write),

        .o_req_dmem         (req_dmem),
        .i_gnt_dmem         (gnt_dmem),
        .o_data_addr        (data_addr),
        .i_data_rd_data     (data_rd_data),
        .o_data_wr_data     (data_wr_data),
        .o_data_size        (data_size),
        .o_data_read        (data_read),
        .o_data_write       (data_write),

        // UART
        .o_data_out_ready   (data_out_ready),
        .o_data_in_valid    (data_in_valid),
        .o_data_in          (data_in)
    );

    // IDS BUS
    ids_bus bus_0 (
        .i_clk          (i_clk), 
        .i_rst_n        (i_rst_n),

    // RV IMEM
        .i_imem_addr    (instr_addr),
        .i_imem_write   (instr_write),
        .i_imem_read    (instr_read),
        .i_imem_size    (instr_size),
        .i_imem_din     (instr_wr_data),
        .o_imem_dout    (instr_rd_data),

    // RV DMEM
        .i_req_dmem     (req_dmem),
        .o_gnt_dmem     (gnt_dmem),
        .i_dmem_addr    (data_addr),
        .i_dmem_write   (data_write),
        .i_dmem_read    (data_read),
        .i_dmem_size    (data_size),
        .i_dmem_din     (data_wr_data),
        .o_dmem_dout    (data_rd_data),

    // DMA
        .i_req_dma      (),
        .o_gnt_dma      (),
        .i_dma_addr     (),
        .i_dma_write    (),
        .i_dma_read     (),
        .i_dma_size     (),
        .i_dma_din      (),
        .o_dma_dout     (),

    // IMEM SRAM (IMEM port)
        .o_imem_addr    (imem_addr),
        .o_imem_write   (imem_write),
        .o_imem_read    (imem_read),
        .o_imem_size    (imem_size),
        .o_imem_din     (imem_wr_data),
        .i_imem_dout    (imem_rd_data),

    // DMEM SRAM (DMEM port)
        .o_dmem_addr    (dmem_addr),
        .o_dmem_write   (dmem_write),
        .o_dmem_read    (dmem_read),
        .o_dmem_size    (dmem_size),
        .o_dmem_din     (dmem_wr_data),
        .i_dmem_dout    (dmem_rd_data)
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

    //UART
    uart #(
        .CLOCK_FREQ     (CPU_CLOCK_FREQ),
        .BAUD_RATE      (BAUD_RATE)
    ) on_chip_uart (
        .clk            (i_clk),
        .reset          (!i_rst_n),

        .data_in        (data_in),
        .data_in_valid  (data_in_valid),
        .data_out_ready (data_out_ready),
        .serial_in      (i_serial_rx),

        .data_in_ready  (data_in_ready),
        .data_out       (data_out),
        .data_out_valid (data_out_valid),
        .serial_out     (o_serial_tx)
    );


endmodule