
module spi_slave(
    input                   i_rst_n,
    input                   i_clk,
    input                   i_sclk,
    input                   i_ss_n,
    input                   i_mosi,
    output                  o_miso,
    input           [31:0]  i_data,
    output  logic   [31:0]  o_data
);

    logic [31:0] RBUF, TBUF;
    logic [31:0] r_dat;
    logic d_ssn;
    logic w_rstn;

    assign o_miso = TBUF[31];

    always_ff @(posedge i_sclk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            RBUF <= 32'h00;
        end else begin
            RBUF <= {RBUF[30:00], i_mosi};
        end
    end

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            d_ssn <= 1'b1;
        end else begin
            d_ssn <= i_ss_n;
        end
    end

    assign w_rstn = ((i_ss_n == 1'b0) && (d_ssn == 1'b1)) ? 1'b0 : 1'b1;

    always_ff @(negedge i_sclk or negedge w_rstn) begin
        if (w_rstn == 1'b0) begin
            TBUF <= r_dat;
        end else begin
            TBUF <= {TBUF[30:00], 1'b0};
        end
    end

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            r_dat <= 32'h00;
            o_data <= 32'h00;
        end else begin
            if (i_ss_n == 1'b1) begin
                  r_dat <= i_data;
                  o_data <= RBUF;
            end
        end
    end

endmodule
