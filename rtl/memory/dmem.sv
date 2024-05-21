module dmem #(
    parameter MEM_DEPTH = 4096,
    parameter MEM_ADDR_WIDTH = 12
) (
    input                   i_clk,
    
    input           [31:0]  i_data_addr,
    output  logic   [31:0]  o_data_rd_data,
    input           [31:0]  i_data_wr_data,
    input           [3:0]   i_data_size,
	input					i_data_write,
	input					i_data_read
);

	sram_4k dmem_sram (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (i_data_read),
		.WEN			(~({4{i_data_write}} & i_data_size)),
		.A 				(i_data_addr[MEM_ADDR_WIDTH-1:2]),
		.D 				(i_data_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(o_data_rd_data)
	);


endmodule