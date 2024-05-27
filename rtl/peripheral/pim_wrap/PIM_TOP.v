module PIM_TOP (
	input i_clk, 
	input i_rst,


	//RISCV I/O
	input [31:0] i_address,
	input [31:0] i_data,
	output [31:0] o_data,

	//weight
	output o_weight_out_en0,
	output o_weight_out_en1,
	output o_weight_out_en2,
	output o_weight_out_en3,
	output [8:0] o_WL_address0,
	output [8:0] o_WL_address1,
	output [8:0] o_WL_address2,
	output [8:0] o_WL_address3,
	output [255:0] o_cam_data0,
	output [255:0] o_cam_data1,
	output [255:0] o_cam_data2,
	output [255:0] o_cam_data3,
	output [255:0] o_cim_data0,
	output [255:0] o_cim_data1,
	output [255:0] o_cim_data2,
	output [255:0] o_cim_data3,

	//activation
	output o_activation_out_en0,
	output o_activation_out_en1,
	output o_activation_out_en2,
	output o_activation_out_en3,
	output [287:0] o_activation_data0,
	output [287:0] o_activation_data1,
	output [287:0] o_activation_data2,
	output [287:0] o_activation_data3,

	//result
	input [8191:0] i_result_in0,
	input [8191:0] i_result_in1,
	input [8191:0] i_result_in2,
	input [8191:0] i_result_in3
);
	
	wire [7:0] counter;
	wire pim_control_read;
	wire busy, valid;

	wire weight_in_en, weight_out_en;
	wire [1:0] weight_sel;
	wire [8:0] WL_address;
	wire [255:0] cam_data;
	wire [255:0] cim_data;

	wire activation_in_en, activation_out_en;
	wire [1:0] activation_sel;
	wire [287:0] activation_data;

	wire result_in_en, result_out_en;
	wire [8191:0] result_in;
	wire [31:0] result_out;

	// always @(*) begin
	// 	if (i_rst) begin
	// 		result_in = 0;
	// 	end else begin
	// 		if (i_result_in0 != 0) begin
	// 			result_in = i_result_in0;
	// 		end else if (i_result_in1 != 0) begin
	// 			result_in = i_result_in1;
	// 		end else if (i_result_in2 != 0) begin
	// 			result_in = i_result_in2;
	// 		end else if (i_result_in3 != 0) begin
	// 			result_in = i_result_in3;
	// 		end else begin
	// 			result_in = 0;
	// 		end
	// 	end
	// end

	pim_controller controller(
		.i_clk					(i_clk), 
		.i_rst					(i_rst),
		.i_address				(i_address),

		.o_weight_in_en			(weight_in_en),	
		.o_weight_out_en		(weight_out_en),
		.o_weight_sel			(weight_sel),
		.o_WL_address			(WL_address),

		.o_activation_in_en		(activation_in_en),
		.o_activation_out_en	(activation_out_en),
		.o_activation_sel		(activation_sel),

		.o_result_in_en			(result_in_en),
		.o_result_out_en		(result_out_en),

		.o_counter				(counter),
		.o_busy					(busy),
		.o_valid				(valid),
		.o_pim_control_read		(pim_control_read)
	);

	wire a1, a2;

	weight_buffer WB (
		.i_clk					(i_clk),
		.i_rst					(i_rst),
		.i_weight_in_en			(weight_in_en),			
		.i_weight_out_en		(weight_out_en),
		.i_counter				(counter[3:0]),
		.i_data					(i_data),
		.o_cam_data				(cam_data),
		.o_cim_data				(cim_data)
	);

	activation_buffer AB (
		.i_clk					(i_clk),
		.i_rst					(i_rst),
		.i_activation_in_en		(activation_in_en),		
		.i_activation_out_en	(activation_out_en),
		.i_counter				(counter),
		.i_data					(i_data),
		.o_data					(activation_data)
	);

	result_buffer RB (
		.i_clk					(i_clk),
		.i_rst					(i_rst),
		.i_result_in_en			(result_in_en),
		.i_result_out_en		(result_out_en),
		.i_counter				(counter),
		.i_data					(result_in),
		.o_data					(result_out)
	);


	dmux  #(
		.width			(256)
	) cam_weight_sel (
		.i_in			(cam_data),
		.i_sel			(weight_sel),
		.o_out0			(o_cam_data0),
		.o_out1			(o_cam_data1),
		.o_out2			(o_cam_data2),
		.o_out3			(o_cam_data3)
	);

	dmux  #(
		.width			(256)
	) cim_weight_sel (
		.i_in			(cim_data),
		.i_sel			(weight_sel),
		.o_out0			(o_cim_data0),
		.o_out1			(o_cim_data1),
		.o_out2			(o_cim_data2),
		.o_out3			(o_cim_data3)
	);

	dmux  #(
		.width			(1)
	) weight_out_sel (
		.i_in			(weight_out_en),
		.i_sel			(weight_sel),
		.o_out0			(o_weight_out_en0),
		.o_out1			(o_weight_out_en1),
		.o_out2			(o_weight_out_en2),
		.o_out3			(o_weight_out_en3)
	);

	dmux  #(
		.width			(9)
	) WL_address_sel (
		.i_in			(WL_address),
		.i_sel			(weight_sel),
		.o_out0			(o_WL_address0),
		.o_out1			(o_WL_address1),
		.o_out2			(o_WL_address2),
		.o_out3			(o_WL_address3)
	);

	dmux  #(
		.width			(1)
	) activation_out_sel (
		.i_in			(activation_out_en),
		.i_sel			(activation_sel),
		.o_out0			(o_activation_out_en0),
		.o_out1			(o_activation_out_en1),
		.o_out2			(o_activation_out_en2),
		.o_out3			(o_activation_out_en3)
	);

	dmux  #(
		.width			(288)
	) activation_data_sel (
		.i_in			(activation_data),
		.i_sel			(activation_sel),
		.o_out0			(o_activation_data0),
		.o_out1			(o_activation_data1),
		.o_out2			(o_activation_data2),
		.o_out3			(o_activation_data3)
	);

	mux #(
		.width			(8192)
	) result_in_sel (
		.i_in0			(i_result_in0),
		.i_in1			(i_result_in1),
		.i_in2			(i_result_in2),
		.i_in3			(i_result_in3),
		.i_sel			(activation_sel),
		.o_out			(result_in)
	);

	assign o_data = pim_control_read ? {30'b0, valid, busy} : result_out;



endmodule