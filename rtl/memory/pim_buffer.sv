module pim_buffer #(
    parameter MEM_DEPTH = 28672,
    parameter MEM_ADDR_WIDTH = 15
) (
    input                   i_clk,

    input           [31:0]  i_buf_addr,
    output  logic   [31:0]  o_buf_rd_data,
    input           [31:0]  i_buf_wr_data,
    input           [3:0]   i_buf_size,
	input					i_buf_write,
	input					i_buf_read
);

	sram_28k buf_sram (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (i_buf_read),
		.WEN			(i_buf_size),
		.A 				(i_buf_addr[MEM_ADDR_WIDTH-1:2]),     // 10-bit address
		.D 				(i_buf_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(o_buf_rd_data)
	);



endmodule