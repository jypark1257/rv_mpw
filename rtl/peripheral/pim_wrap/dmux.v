module dmux #(
	parameter width = 256
) (
	input [width-1:0]i_in,
	input [1:0] i_sel,
	output reg [width-1:0] o_out0,
	output reg [width-1:0] o_out1,
	output reg [width-1:0] o_out2,
	output reg [width-1:0] o_out3
);

	always @(*) begin
		case (i_sel) 
			2'b00: begin
				o_out0 = i_in;
				o_out1 = 0;
				o_out2 = 0;
				o_out3 = 0;
			end
			2'b01: begin
				o_out0 = 0;
				o_out1 = i_in;
				o_out2 = 0;
				o_out3 = 0;
			end
			2'b10: begin
				o_out0 = 0;
				o_out1 = 0;
				o_out2 = i_in;
				o_out3 = 0;
			end
			2'b11: begin
				o_out0 = 0;
				o_out1 = 0;
				o_out2 = 0;
				o_out3 = i_in;
			end
			default: begin
				o_out0 = 0;
				o_out1 = 0;
				o_out2 = 0;
				o_out3 = 0;
			end
		endcase
	end


endmodule

module mux #(
	parameter width = 256
) (
	input [width-1:0]i_in0,
	input [width-1:0]i_in1,
	input [width-1:0]i_in2,
	input [width-1:0]i_in3,
	input [1:0] i_sel,
	output reg [width-1:0] o_out
);

	always @(*) begin
		case (i_sel) 
			2'b00: begin
				o_out = i_in0;
			end
			2'b01: begin
				o_out = i_in1;
			end
			2'b10: begin
				o_out = i_in2;
			end
			2'b11: begin
				o_out = i_in3;
			end
			default: begin
				o_out = 0;
			end
		endcase
	end


endmodule