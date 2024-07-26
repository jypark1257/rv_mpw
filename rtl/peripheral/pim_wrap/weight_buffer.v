module BL_driver (
	input CLK,
	input RSTN,
	input i_weight_in_en,
	input i_weight_out_en,
	input [3:0] i_counter,
	input [15:0] i_data,
	output reg o_weight_out_en,
	output reg [255:0] o_data
);

	reg [255:0] BL_data;

	always @(*) begin
		if (!RSTN) begin
			BL_data = 0;
		end else begin
			if (i_weight_in_en) begin
				if (i_counter == 4'd0) begin
					BL_data[255:240] = i_data;
				end else if (i_counter == 4'd1) begin
					BL_data[239:224] = i_data;
				end else if (i_counter == 4'd2) begin
					BL_data[223:208] = i_data;
				end else if (i_counter == 4'd3) begin
					BL_data[207:192] = i_data;
				end else if (i_counter == 4'd4) begin
					BL_data[191:176] = i_data;
				end else if (i_counter == 4'd5) begin
					BL_data[175:160] = i_data;
				end else if (i_counter == 4'd6) begin
					BL_data[159:144] = i_data;
				end else if (i_counter == 4'd7) begin
					BL_data[143:128] = i_data;
				end else if (i_counter == 4'd8) begin
					BL_data[127:112] = i_data;
				end else if (i_counter == 4'd9) begin
					BL_data[111:96] = i_data;
				end else if (i_counter == 4'd10) begin
					BL_data[95:80] = i_data;
				end else if (i_counter == 4'd11) begin
					BL_data[79:64] = i_data;
				end else if (i_counter == 4'd12) begin
					BL_data[63:48] = i_data;
				end else if (i_counter == 4'd13) begin
					BL_data[47:32] = i_data;
				end else if (i_counter == 4'd14) begin
					BL_data[31:16] = i_data;
				end else if (i_counter == 4'd15) begin
					BL_data[15:0] = i_data;
				end
			end else begin
				BL_data = 0;
			end
		end
	end

	always @(posedge CLK) begin
		if (!RSTN) begin
			o_data <= 0;
			o_weight_out_en <= 0;
		end else begin
			o_weight_out_en <= i_weight_out_en;
			if (i_weight_out_en) begin
				o_data <= BL_data;
			end
		end
	end

endmodule



// module weight_buffer (
// 	input CLK,
// 	input !RSTN,
// 	input i_weight_buffer_busy,
// 	input i_weight_in_en,
// 	input i_weight_out_en,
// 	input [3:0] i_counter,
// 	input [31:0] i_data,
// 	output [255:0] o_cam_data,
// 	output [255:0] o_mac_data
// );

// 	reg [255:0] cam_data;
// 	reg [255:0] mac_data;

// 	always @(posedge CLK) begin
// 		if (!RSTN) begin
// 			cam_data <= 0;
// 			mac_data <= 0;
// 		end else begin
// 			if (i_weight_buffer_busy) begin
// 				if (i_weight_in_en) begin
// 					if (i_counter == 4'd0) begin
// 						cam_data[255:240] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[255:240] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd1) begin
// 						cam_data[239:224] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[239:224] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd2) begin
// 						cam_data[223:208] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[223:208] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd3) begin
// 						cam_data[207:192] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[207:192] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd4) begin
// 						cam_data[191:176] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[191:176] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd5) begin
// 						cam_data[175:160] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[175:160] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd6) begin
// 						cam_data[159:155] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[159:155] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd7) begin
// 						cam_data[154:128] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[154:128] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd8) begin
// 						cam_data[127:112] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[127:112] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd9) begin
// 						cam_data[111:96] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[111:96] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd10) begin
// 						cam_data[95:80] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[95:80] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd11) begin
// 						cam_data[79:64] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[79:64] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd12) begin
// 						cam_data[63:48] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[63:48] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd13) begin
// 						cam_data[47:32] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[47:32] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd14) begin
// 						cam_data[31:16] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[31:16] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd15) begin
// 						cam_data[15:0] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[15:0] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end
// 				end
// 			end else begin
// 				cam_data <= 0;
// 				mac_data <= 0;
// 			end	
// 		end
// 	end

// 	assign o_cam_data = i_weight_out_en ? cam_data : 255'b0;
// 	assign o_mac_data = i_weight_out_en ? mac_data : 255'b0;

// endmodule



// module weight_buffer (
// 	input CLK,
// 	input !RSTN,
// 	input i_weight_buffer_busy,
// 	input i_weight_in_en,
// 	input i_weight_out_en,
// 	input [3:0] i_counter,
// 	input [31:0] i_data,
// 	output [255:0] o_cam_data,
// 	output [255:0] o_mac_data
// );

// 	reg [255:0] cam_data;
// 	reg [255:0] mac_data;

// 	always @(posedge CLK) begin
// 		if (!RSTN) begin
// 			cam_data <= 0;
// 			mac_data <= 0;
// 		end else begin
// 			if (i_weight_buffer_busy) begin
// 				if (i_weight_in_en) begin
// 					if (i_counter == 4'd0) begin
// 						cam_data[255:240] <= i_data[31:16];
// 						mac_data[255:240] <= i_data[15:0];
// 					end else if (i_counter == 4'd1) begin
// 						cam_data[239:224] <= i_data[31:16];
// 						mac_data[239:224] <= i_data[15:0];
// 					end else if (i_counter == 4'd2) begin
// 						cam_data[223:208] <= i_data[31:16];
// 						mac_data[223:208] <= i_data[15:0];
// 					end else if (i_counter == 4'd3) begin
// 						cam_data[207:192] <= i_data[31:16];
// 						mac_data[207:192] <= i_data[15:0];
// 					end else if (i_counter == 4'd4) begin
// 						cam_data[191:176] <= i_data[31:16];
// 						mac_data[191:176] <= i_data[15:0];
// 					end else if (i_counter == 4'd5) begin
// 						cam_data[175:160] <= i_data[31:16];
// 						mac_data[175:160] <= i_data[15:0];
// 					end else if (i_counter == 4'd6) begin
// 						cam_data[159:155] <= i_data[31:16];
// 						mac_data[159:155] <= i_data[15:0];
// 					end else if (i_counter == 4'd7) begin
// 						cam_data[154:128] <= i_data[31:16];
// 						mac_data[154:128] <= i_data[15:0];
// 					end else if (i_counter == 4'd8) begin
// 						cam_data[127:112] <= i_data[31:16];
// 						mac_data[127:112] <= i_data[15:0];
// 					end else if (i_counter == 4'd9) begin
// 						cam_data[111:96] <= i_data[31:16];
// 						mac_data[111:96] <= i_data[15:0];
// 					end else if (i_counter == 4'd10) begin
// 						cam_data[95:80] <= i_data[31:16];
// 						mac_data[95:80] <= i_data[15:0];
// 					end else if (i_counter == 4'd11) begin
// 						cam_data[79:64] <= i_data[31:16];
// 						mac_data[79:64] <= i_data[15:0];
// 					end else if (i_counter == 4'd12) begin
// 						cam_data[63:48] <= i_data[31:16];
// 						mac_data[63:48] <= i_data[15:0];
// 					end else if (i_counter == 4'd13) begin
// 						cam_data[47:32] <= i_data[31:16];
// 						mac_data[47:32] <= i_data[15:0];
// 					end else if (i_counter == 4'd14) begin
// 						cam_data[31:16] <= i_data[31:16];
// 						mac_data[31:16] <= i_data[15:0];
// 					end else if (i_counter == 4'd15) begin
// 						cam_data[15:0] <= i_data[31:16];
// 						mac_data[15:0] <= i_data[15:0];
// 					end
// 				end
// 			end else begin
// 				cam_data <= 0;
// 				mac_data <= 0;
// 			end	
// 		end
// 	end

// 	assign o_cam_data = i_weight_out_en ? cam_data : 255'b0;
// 	assign o_mac_data = i_weight_out_en ? mac_data : 255'b0;

// endmodule






// module weight_buffer (
// 	input CLK,
// 	input !RSTN,
// 	input i_weight_buffer_busy,
// 	input i_weight_in_en,
// 	input i_weight_out_en,
// 	input [3:0] i_counter,
// 	input [31:0] i_data,
// 	output [255:0] o_cam_data,
// 	output [255:0] o_mac_data
// );

// 	reg [255:0] cam_data;
// 	reg [255:0] mac_data;

// 	always @(posedge CLK) begin
// 		if (!RSTN) begin
// 			cam_data <= 0;
// 			mac_data <= 0;
// 		end else begin
// 			if (i_weight_buffer_busy) begin
// 				if (i_weight_in_en) begin
// 					if (i_counter == 4'd0) begin
// 						cam_data[255:240] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[255:240] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd1) begin
// 						cam_data[239:224] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[239:224] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd2) begin
// 						cam_data[223:208] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[223:208] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd3) begin
// 						cam_data[207:192] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[207:192] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd4) begin
// 						cam_data[191:176] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[191:176] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd5) begin
// 						cam_data[175:160] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[175:160] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd6) begin
// 						cam_data[159:155] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[159:155] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd7) begin
// 						cam_data[154:128] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[154:128] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd8) begin
// 						cam_data[127:112] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[127:112] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd9) begin
// 						cam_data[111:96] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[111:96] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd10) begin
// 						cam_data[95:80] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[95:80] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd11) begin
// 						cam_data[79:64] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[79:64] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd12) begin
// 						cam_data[63:48] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[63:48] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd13) begin
// 						cam_data[47:32] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[47:32] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd14) begin
// 						cam_data[31:16] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[31:16] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end else if (i_counter == 4'd15) begin
// 						cam_data[15:0] <= {i_data[31:28], i_data[23:20], i_data[15:12], i_data[7:4]};
// 						mac_data[15:0] <= {i_data[27:24], i_data[19:16], i_data[11:8], i_data[3:0]};
// 					end
// 				end
// 			end else begin
// 				cam_data <= 0;
// 				mac_data <= 0;
// 			end	
// 		end
// 	end

// 	assign o_cam_data = i_weight_out_en ? cam_data : 255'b0;
// 	assign o_mac_data = i_weight_out_en ? mac_data : 255'b0;

// endmodule


