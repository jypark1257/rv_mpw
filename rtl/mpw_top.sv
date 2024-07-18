


module mpw_top (
    input                       i_clk,
    // CORE RESET
    input                       i_rv_rst_n,
    
    // SPI RESET
    input                       i_spi_rst_n,

    // SPI
    input                       sclk,
    input                       cs,
    input                       mosi,
    output logic                miso,

    // UART
    input                       i_serial_rx,
    output logic                o_serial_tx

);

    logic [31:0] pim_addr;
    logic [31:0] pim_wr_data;
    logic [31:0] pim_rd_data;

    core_top #(
        .XLEN(32),
        .CPU_CLOCK_FREQ(250_000_000),
        .RESET_PC(32'h4000_0000),
        .BAUD_RATE(115200)
    ) core_top_0 (
    .i_clk              (i_clk),
    // CORE RESET
    .i_rv_rst_n         (i_rv_rst_n),
    
    // SPI RESET
    .i_spi_rst_n        (i_spi_rst_n),

    // SPI
    .i_sclk             (sclk),
    .i_cs               (cs),
    .i_mosi             (mosi),
    .o_miso             (miso),

    // UART
    .i_serial_rx        (i_serial_rx),
    .o_serial_tx        (o_serial_tx),

    // PIM I/F
    .o_pim_addr         (pim_addr),
    .o_pim_wr_data      (pim_wr_data),
    .i_pim_rd_data      (pim_rd_data)
    );

    PIM_TOP pim_top_0 (
        .i_clk(i_clk),
        .i_rst(!i_rv_rst_n),

        .i_address(pim_addr),
        .i_data(pim_wr_data),
        .o_data(pim_rd_data)
    );


endmodule

