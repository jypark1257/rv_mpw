module weight_buffer (
	input i_clk,
	input i_rst,
	input i_weight_in_en,
	input i_weight_out_en,
	input [3:0] i_counter,
	input [31:0] i_data,
	output [255:0] o_cam_data,
	output [255:0] o_cim_data
);

	reg [255:0] cam_data;
	reg [255:0] cim_data;

	always @(posedge i_clk) begin
		if (i_rst) begin
			cam_data <= 0;
			cim_data <= 0;
		end else begin
			if (i_weight_in_en) begin
				if (i_counter == 4'd0) begin
					cam_data[255:240] <= i_data[31:16];
					cim_data[255:240] <= i_data[15:0];
				end else if (i_counter == 4'd1) begin
					cam_data[239:224] <= i_data[31:16];
					cim_data[239:224] <= i_data[15:0];
				end else if (i_counter == 4'd2) begin
					cam_data[223:208] <= i_data[31:16];
					cim_data[223:208] <= i_data[15:0];
				end else if (i_counter == 4'd3) begin
					cam_data[207:192] <= i_data[31:16];
					cim_data[207:192] <= i_data[15:0];
				end else if (i_counter == 4'd4) begin
					cam_data[191:176] <= i_data[31:16];
					cim_data[191:176] <= i_data[15:0];
				end else if (i_counter == 4'd5) begin
					cam_data[175:160] <= i_data[31:16];
					cim_data[175:160] <= i_data[15:0];
				end else if (i_counter == 4'd6) begin
					cam_data[159:155] <= i_data[31:16];
					cim_data[159:155] <= i_data[15:0];
				end else if (i_counter == 4'd7) begin
					cam_data[154:128] <= i_data[31:16];
					cim_data[154:128] <= i_data[15:0];
				end else if (i_counter == 4'd8) begin
					cam_data[127:112] <= i_data[31:16];
					cim_data[127:112] <= i_data[15:0];
				end else if (i_counter == 4'd9) begin
					cam_data[111:96] <= i_data[31:16];
					cim_data[111:96] <= i_data[15:0];
				end else if (i_counter == 4'd10) begin
					cam_data[95:80] <= i_data[31:16];
					cim_data[95:80] <= i_data[15:0];
				end else if (i_counter == 4'd11) begin
					cam_data[79:64] <= i_data[31:16];
					cim_data[79:64] <= i_data[15:0];
				end else if (i_counter == 4'd12) begin
					cam_data[63:48] <= i_data[31:16];
					cim_data[63:48] <= i_data[15:0];
				end else if (i_counter == 4'd13) begin
					cam_data[47:32] <= i_data[31:16];
					cim_data[47:32] <= i_data[15:0];
				end else if (i_counter == 4'd14) begin
					cam_data[31:16] <= i_data[31:16];
					cim_data[31:16] <= i_data[15:0];
				end else if (i_counter == 4'd15) begin
					cam_data[15:0] <= i_data[31:16];
					cim_data[15:0] <= i_data[15:0];
				end
			end
		end
	end

	assign o_cam_data = i_weight_out_en ? cam_data : 255'b0;
	assign o_cim_data = i_weight_out_en ? cim_data : 255'b0;

endmodule


