
module uart_wrap #(
    parameter CLOCK_FREQ    = 125_000_000,
    parameter BAUD_RATE     = 115_200,
    parameter UART_CTRL     = 32'h8000_0000,
    parameter UART_RECV     = 32'h8000_0004,
    parameter UART_TRANS    = 32'h8000_0008
) (
    input                   i_clk, 
    input                   i_rst_n, 

    input           [31:0]  i_uart_addr,
    input                   i_uart_write,
    input                   i_uart_read,
    input           [ 3:0]  i_uart_size,
    input           [31:0]  i_uart_din,
    output logic    [31:0]  o_uart_dout,

    // serial IO
    input                   i_serial_rx,
    output logic            o_serial_tx
);

    logic [31:0] uart_addr;
    logic uart_read;

    // inputs
    logic [7:0] data_in;
    logic data_in_valid;
    logic data_out_ready;

    // outputs
    logic [7:0] data_out;
    logic data_in_ready;
    logic data_out_valid;

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            uart_addr <= '0;
            uart_read <= '0;
        end else begin
            uart_addr <= i_uart_addr;
            uart_read <= i_uart_read;
        end
    end
    
    // assign inputs
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            data_in <= '0;
            data_in_valid <= '0;
            data_out_ready <= '0;
        end else begin
            data_in <= ((i_uart_addr == UART_TRANS) && (i_uart_write)) ? i_uart_din[7:0] : data_in;
            data_in_valid <= ((i_uart_addr == UART_TRANS) && (i_uart_write));
            data_out_ready <= ((i_uart_addr == UART_RECV) && (i_uart_read));
        end
    end

    always_comb begin
        if (uart_read == '0) begin
            o_uart_dout = '0;
        end else begin
            case (uart_addr)
                UART_CTRL: begin    
                    o_uart_dout = {30'b0, data_out_valid, data_in_ready};
                end
                UART_RECV: begin
                    o_uart_dout = {24'b0, data_out};
                end
                default: begin
                    o_uart_dout = '0;
                end
            endcase
        end
    end

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            uart_addr <= '0;
        end else begin
            uart_addr <= i_uart_addr;
        end
    end


    //UART
    uart #(
        .CLOCK_FREQ(CLOCK_FREQ),
        .BAUD_RATE(BAUD_RATE)
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