module activation_buffer (
	input CLK,
	input RSTN,
	input i_activation_in_en,
	input i_activation_out_en,
	input [7:0] i_counter,
	input [31:0] i_data,
	output reg o_activation_out_en,
	output reg [287:0] o_data
);

	reg [287:0] buffer;

	always @(*) begin
		if(!RSTN) begin
			buffer = 0;
		end else begin
			if (i_activation_in_en) begin
				case (i_counter) 
					8'd0: begin
						buffer[287:256] = i_data;
					end
					8'd1: begin
						buffer[255:224] = i_data;
					end
					8'd2: begin
						buffer[223:192] = i_data;
					end
					8'd3: begin
						buffer[191:160] = i_data;
					end
					8'd4: begin
						buffer[159:128] = i_data;
					end
					8'd5: begin
						buffer[127:96] = i_data;
					end
					8'd6: begin
						buffer[95:64] = i_data;
					end	
					8'd7: begin
						buffer[63:32] = i_data;
					end
					8'd8: begin
						buffer[31:0] = i_data;
					end
				endcase
			end
		end
	end

	always @(posedge CLK) begin
		if (!RSTN) begin
			o_data <= 0;
			o_activation_out_en <= 0;
		end else begin
			o_activation_out_en <= i_activation_out_en;
			if (i_activation_out_en) begin
				o_data <= buffer;
			end
		end
	end


endmodule



// module activation_buffer (
// 	input CLK,
// 	input RSTN,
// 	input i_activation_buffer_busy,
// 	input i_activation_in_en,
// 	input i_activation_out_en,
// 	input [7:0] i_counter,
// 	input [31:0] i_data,
// 	output [287:0] o_data
// );

// 	reg [287:0] buffer;

// 	always @(posedge CLK) begin
// 		if(RSTN) begin
// 			buffer <= 0;
// 		end else begin
// 			if (i_activation_buffer_busy) begin
// 				if (i_activation_in_en) begin
// 					case (i_counter) 
// 						8'd0: begin
// 							buffer[287:256] <= i_data;
// 						end
// 						8'd1: begin
// 							buffer[255:224] <= i_data;
// 						end
// 						8'd2: begin
// 							buffer[223:192] <= i_data;
// 						end
// 						8'd3: begin
// 							buffer[191:160] <= i_data;
// 						end
// 						8'd4: begin
// 							buffer[191:160] <= i_data;
// 						end
// 						8'd5: begin
// 							buffer[159:128] <= i_data;
// 						end
// 						8'd6: begin
// 							buffer[127:96] <= i_data;
// 						end	
// 						8'd7: begin
// 							buffer[63:32] <= i_data;
// 						end
// 						8'd8: begin
// 							buffer[31:0] <= i_data;
// 						end
// 					endcase
// 				end
// 			end else begin 
// 				buffer <= 0;
// 			end
// 		end
// 	end

// 	// always @(posedge CLK) begin
// 	// 	if(RSTN) begin
// 	// 		buffer <= 0;
// 	// 	end else begin
// 	// 		if (i_activation_buffer_busy) begin
// 	// 			if (i_activation_in_en) begin
// 	// 				if (i_counter == 8'd0) begin
// 	// 					buffer[287:256] <= i_data;
// 	// 				end else if (i_counter == 8'd1) begin
// 	// 					buffer[255:224] <= i_data;
// 	// 				end else if (i_counter == 8'd2) begin
// 	// 					buffer[223:192] <= i_data;
// 	// 				end else if (i_counter == 8'd3) begin
// 	// 					buffer[191:160] <= i_data;
// 	// 				end else if (i_counter == 8'd4) begin
// 	// 					buffer[159:128] <= i_data;
// 	// 				end else if (i_counter == 8'd5) begin
// 	// 					buffer[127:96] <= i_data;
// 	// 				end else if (i_counter == 8'd6) begin
// 	// 					buffer[95:64] <= i_data;
// 	// 				end else if (i_counter == 8'd7) begin
// 	// 					buffer[63:32] <= i_data;
// 	// 				end else if (i_counter == 8'd8) begin
// 	// 					buffer[31:0] <= i_data;
// 	// 				end
// 	// 			end
// 	// 		end else begin 
// 	// 			buffer <= 0;
// 	// 		end
// 	// 	end
// 	// end

// 	assign o_data = i_activation_out_en ? buffer : 288'b0;

// endmodule

