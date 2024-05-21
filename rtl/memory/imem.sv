module imem #(
    parameter MEM_DEPTH = 4096,
    parameter MEM_ADDR_WIDTH = 12
) (
    input                   i_clk,

    input           [31:0]  i_instr_addr,
    output  logic   [31:0]  o_instr_rd_data,
    input           [31:0]  i_instr_wr_data,
    input           [3:0]   i_instr_size,
	input					i_instr_write,
	input					i_instr_read
);

	sram_4k imem_sram (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (i_instr_read),
		.WEN			(i_instr_size),
		.A 				(i_instr_addr[MEM_ADDR_WIDTH-1:2]),     // 10-bit address
		.D 				(i_instr_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(o_instr_rd_data)
	);



endmodule