`timescale 1ns / 1ps

module fpga_top(
    input sysclk_n,
    input sysclk_p,
    input i_rst_n,
    input i_spi_rst_n,

    // SPI
    input i_sclk,
    input i_cs,
    input i_mosi,
    output o_miso,

    // LEDs
    output reg rst_led,
    output reg spi_rst_led,
    output reg sclk_led,
    output reg cs_led,
    output reg mosi_led,
    output reg miso_led,
    output reg tx_led, 
    output reg rx_led,
    
    // UART TX/RX 
    input i_serial_rx,
    output o_serial_tx
    );    
    
    wire sysclk;
    wire cpu_tx, cpu_rx;
    wire sclk, cs, mosi, miso;

    // SPI IOB
    (* IOB = "true" *) reg fpga_sclk_iob;
    (* IOB = "true" *) reg fpga_cs_iob;
    (* IOB = "true" *) reg fpga_mosi_iob;
    (* IOB = "true" *) reg fpga_miso_iob;


    // UART IOB
    (* IOB = "true" *) reg fpga_serial_tx_iob;
    (* IOB = "true" *) reg fpga_serial_rx_iob;

    
    always @(posedge sysclk or negedge i_spi_rst_n) begin
        if (~i_spi_rst_n) begin
            spi_rst_led <= 1'b0;
            sclk_led <= 1'b0;
            cs_led <= 1'b0;
            mosi_led <= 1'b0;
            miso_led <= 1'b0;
        end else begin
            spi_rst_led <= 1'b1;
            sclk_led <= fpga_sclk_iob;
            cs_led <= fpga_cs_iob;
            mosi_led <= fpga_mosi_iob;
            miso_led <= fpga_miso_iob;
        end
    end

    always @(posedge sysclk or negedge i_rst_n) begin
        if (~i_rst_n) begin
            rst_led <= 1'b0;
            tx_led <= 1'b0;
            rx_led <= 1'b0;
        end else begin
            rst_led <= 1'b1;
            tx_led <= ~fpga_serial_tx_iob;
            rx_led <= ~fpga_serial_rx_iob;
        end
    end
    
    

    clk_wiz_0 u_clk_wiz (
        .clk_out1(sysclk),
        .clk_in1_p(sysclk_p),
        .clk_in1_n(sysclk_n)
    );

    //RVCORE_TOP #(
    //.CPU_CLOCK_FREQ(30_000_000)
    //) u_core_top (
    //    .clk(sysclk),
    //    .rst(i_rst_n),
    //    
    //    .FPGA_SERIAL_RX(cpu_rx),
    //    .FPGA_SERIAL_TX(cpu_tx)
    //);

    core_top #(
        .CPU_CLOCK_FREQ(25_000_000),
        .BAUD_RATE  (9600)
    ) u_core_top (
        .i_clk(sysclk),
        .i_rv_rst_n(i_rst_n),
        .i_spi_rst_n(i_spi_rst_n),

        // SPI
        .i_sclk(sclk),
        .i_cs(cs),
        .i_mosi(mosi),
        .o_miso(miso),

        .i_serial_rx(cpu_rx),
        .o_serial_tx(cpu_tx)
    );


    // SPI IOB assign
    assign o_miso = fpga_miso_iob;
    assign sclk = fpga_sclk_iob;
    assign cs = fpga_cs_iob;
    assign mosi = fpga_mosi_iob;
    always @(posedge sysclk) begin
        fpga_miso_iob <= miso;
        fpga_sclk_iob <= i_sclk;
        fpga_cs_iob <= i_cs;
        fpga_mosi_iob <= i_mosi;
    end



    // UART IOB assign
    assign o_serial_tx = fpga_serial_tx_iob;
    assign cpu_rx = fpga_serial_rx_iob;
    always @(posedge sysclk) begin
        fpga_serial_tx_iob <= cpu_tx;
        fpga_serial_rx_iob <= i_serial_rx;
    end

    
endmodule



