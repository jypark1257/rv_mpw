
module register_file #(
    parameter XLEN = 32
) (
    input                       i_clk,
    input                       i_rst_n,
    input           [4:0]       i_rs1,
    input           [4:0]       i_rs2,
    input           [4:0]       i_rd,
    input           [XLEN-1:0]  i_rd_din,
    input                       i_reg_write,
    output          [XLEN-1:0]  o_rs1_dout,
    output          [XLEN-1:0]  o_rs2_dout
);

    logic [XLEN-1:0] rf_data[0:31];

    int i;
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            for (i = 0; i < 32; i = i + 1) begin
                rf_data[i] <= '0;
            end
        end else begin
            if (i_reg_write) begin
                if(i_rd == '0) begin
                    rf_data[i_rd] <= '0;            // hard-wired ZERO
                end else begin
                    rf_data[i_rd] <= i_rd_din;
                end
            end else begin
                rf_data[i_rd] <= rf_data[i_rd];
            end
        end
    end

    // output logic for rs1
    assign o_rs1_dout = (i_reg_write && (i_rs1 == i_rd)) ? i_rd_din : rf_data[i_rs1];

    // output logic for rs2
    assign o_rs2_dout = (i_reg_write && (i_rs2 == i_rd)) ? i_rd_din : rf_data[i_rs2];

endmodule