module pim_controller (
	input i_clk, 
	input i_rst,
	input [31:0] i_address,

	output reg o_weight_in_en,
	output reg o_weight_out_en,
	output reg [1:0] o_weight_sel,
	output reg [8:0] o_WL_address,

	output reg o_activation_in_en,
	output reg o_activation_out_en,
	output reg [1:0] o_activation_sel,

	output reg o_result_in_en,
	output reg o_result_out_en,
	

	output reg [7:0] o_counter,
	output reg o_busy,
	output reg o_valid,
	output o_pim_control_read
);

	//counter
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_counter <= 0;
		end else begin
			if (weight_in_en) begin 
				if (o_weight_in_en) begin 
					o_counter <= o_counter + 1;
				end
			end else if (activation_in_en) begin 
				if (o_activation_in_en) begin 
					o_counter  <= o_counter + 1;
				end
			end else if (compute_en) begin 
				o_counter <= o_counter + 1;
			end	else if (result_in_en) begin
				o_counter <= o_counter + 1;
			end else if (result_out_en) begin
				if (o_result_out_en) begin
					o_counter <= o_counter + 1;
				end
			end	else begin
				o_counter <= 0;
			end
		end
	end

	//busy
	always @(*) begin
		if (i_rst) begin
			o_busy = 0;
		end else begin
			if (weight_in_en) begin 
				o_busy = 1;
			end else if (activation_in_en) begin 
				o_busy = 1;
			end else if (compute_en | compute_en_q) begin 
				o_busy = 1;
			end	else if (result_in_en) begin
				o_busy = 1;
			end else if (result_out_en) begin
				o_busy = 1;
			end	else begin
				o_busy = 0;
			end
		end
	end
	
	//valid
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_valid <= 0;
		end else begin
			if(o_result_in_en) begin
				o_valid <= 1;
			end
			if (result_out_en_1) begin
				o_valid <= 0;
			end
		end
	end

	//PIM_control
	reg o_pim_control_read;
	always @(posedge i_clk) begin
		if (i_address == 32'h4000_0010) begin
			o_pim_control_read <= 1;
		end else begin
			o_pim_control_read <= 0;
		end
	end

	//weight_in_en signal generate
	always @(*) begin
		case (i_address) 
			32'h4000_0041: begin
				o_weight_in_en = 1;
			end
			32'h4000_0042: begin
				o_weight_in_en = 1;
			end
			32'h4000_0044: begin
				o_weight_in_en = 1;
			end
			32'h4000_0048: begin
				o_weight_in_en = 1;
			end
			default: begin
				o_weight_in_en = 0;
			end
		endcase
	end

	//o_weight_out_en
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_weight_out_en <= 0;
		end else begin
			if (weight_in_en) begin 
				if (o_weight_in_en) begin 
					if (o_counter[3:0] == 4'd15) begin 
						o_weight_out_en <= 1;
					end else begin
						o_weight_out_en <= 0;
					end
				end else begin
					o_weight_out_en <= 0;
				end
			end else begin
				o_weight_out_en <= 0;
			end
		end
 	end

	//weight select
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_weight_sel <= 0;
		end else begin
			if (o_weight_in_en) begin
				case (i_address) 
					32'h4000_0041: begin
						o_weight_sel <= 2'b00;
					end
					32'h4000_0042: begin
						o_weight_sel <= 2'b01;
					end
					32'h4000_0044: begin
						o_weight_sel <= 2'b10;
					end
					32'h4000_0048: begin
						o_weight_sel <= 2'b11;
					end
					default: begin
						o_weight_sel <= 2'b00;
					end
				endcase
			end
		end
	end


	//o_WL_address 
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_WL_address <= 0;
		end else begin
			if (o_weight_out_en) begin 
				if (o_WL_address == 9'd287) begin //287로 바꾸기!!!
					o_WL_address <= 0;
				end else begin
					o_WL_address <= o_WL_address + 1;
				end
			end
		end
	end
	

	//activation_in_en signal generate
	always @(*) begin
		case (i_address) 
			32'h4000_0081: begin
				o_activation_in_en = 1;
			end
			32'h4000_0082: begin
				o_activation_in_en = 1;
			end
			32'h4000_0084: begin
				o_activation_in_en = 1;
			end
			32'h4000_0088: begin
				o_activation_in_en = 1;
			end
			default: begin
				o_activation_in_en = 0;
			end
		endcase
	end

	//o_activation_out_en
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_activation_out_en <= 0;
		end else begin
			if (compute_en) begin 
				o_counter <= o_counter +1;
				if (o_counter[2:0] == 3'b111) begin
					o_activation_out_en <= 1;
				end else begin
					o_activation_out_en <= 0;
				end	
			end	else begin
				o_activation_out_en <= 0;
			end
		end
 	end

	//activation select
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_activation_sel <= 0;
		end else begin
			if (o_activation_in_en) begin
				case (i_address) 
					32'h4000_0081: begin
						o_activation_sel <= 2'b00;
					end
					32'h4000_0082: begin
						o_activation_sel <= 2'b01;
					end
					32'h4000_0084: begin
						o_activation_sel <= 2'b10;
					end
					32'h4000_0088: begin
						o_activation_sel <= 2'b11;
					end
					default: begin
						o_activation_sel <= 2'b00;
					end
				endcase
			end
		end
	end

	//compute_en_q
	reg compute_en_q;
	always @(posedge i_clk) begin
		if (i_rst) begin
			compute_en_q <= 0;
		end else begin
			if (activation_in_en) begin 
				if (o_counter == 8'd72) begin
					compute_en_q <= 1;
				end
			end else if (compute_en) begin 
				if (o_counter == 8'd63) begin
					compute_en_q <= 0;
				end
			end	
		end
 	end

	//result_in_en
	reg result_in_en;
	always @(posedge i_clk) begin
		if (i_rst) begin
			result_in_en <= 0;
		end else begin
			if (compute_en) begin 
				if (o_counter == 8'd64) begin
					result_in_en <= 1;
				end
			end	else if (o_result_in_en) begin
				result_in_en <= 0;
			end
		end
 	end

	//o_result_in_en
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_result_in_en <= 0;
		end else begin
			if (result_in_en) begin
				if (o_counter == 8'd71) begin
					o_result_in_en <= 1;
				end else begin
					o_result_in_en <= 0;
				end
			end
		end
 	end

	//result_out
	always @(*) begin
		if (i_rst) begin
			result_out_en_1 = 0;
		end else begin
			if (i_address == 32'h4000_0020) begin
				result_out_en_1 = 1;
			end else begin
				result_out_en_1 = 0;
			end
		end
	end


	reg compute_en;
	reg weight_in_en_d, activation_in_en_d;
	reg result_out_en_1, result_out_en_2;
	
	wire weight_in_en, activation_in_en;
	wire result_out_en;
	
	assign weight_in_en = o_weight_in_en | weight_in_en_d;
	assign activation_in_en = o_activation_in_en | activation_in_en_d;
	assign result_out_en = o_result_out_en | result_out_en_2;
	
	always @(posedge i_clk) begin
		if (i_rst) begin
			compute_en <= 0;
			weight_in_en_d <= 0;
			activation_in_en_d <= 0;
			o_result_out_en <= 0;
			result_out_en_2 <= 0;
		end else begin
			compute_en <= compute_en_q;
			weight_in_en_d <= o_weight_in_en;
			activation_in_en_d <= o_activation_in_en;
			o_result_out_en <= result_out_en_1;
			result_out_en_2 <= o_result_out_en;
		end
	end

	


endmodule






/*
module pim_controller (
	input i_clk, 
	input i_rst,
	input i_weight_en,
	input i_activation_en,
	input i_compute_en,
	output reg o_weight_out_en,
	output reg o_activation_out_en,
	output reg o_output_in_en,
	output reg [6:0] o_counter,
	output reg [1:0] o_weight_sel,
	output reg [8:0] o_WL_address
);

	reg output_in_en, output_in_en_d;
	// reg compute_en, compute_en_d;

	always @(posedge i_clk) begin
		if (i_rst) begin
			o_counter <= 0;
			o_WL_address <= 9'b111111111;
			o_weight_out_en <= 0;
			o_activation_out_en <= 0;
			o_output_in_en <= 0;
			output_in_en <= 0;
			output_in_en_d <= 0;
			// compute_en <= 0;
			// compute_en_d <= 0;
			o_weight_sel <= 0;
		end else begin
			output_in_en_d <= output_in_en;
			// compute_en_d <= compute_en;
			if (i_weight_en) begin //store weight to pim
				o_counter <= o_counter + 1;
				if (o_counter[3:0] == 4'd15) begin 
					o_weight_out_en <= 1;
					o_WL_address <= o_WL_address + 1;
				end else begin
					o_weight_out_en <= 0;
				end
			end else if (i_activation_en) begin //load activation to buffer
				o_counter  <= o_counter + 1;
				// if (o_counter == 7'd71) begin
				// 	compute_en <= 1;
				// end
			end else if (i_compute_en) begin //load atctivation to pim
				o_counter <= o_counter +1;
				if (o_counter[2:0] == 3'b111) begin
					o_activation_out_en <= 1;
				end else begin
					o_activation_out_en <= 0;
				end	
				if (o_counter == 7'd63) begin
					output_in_en <= 1;
				end
			end	else if (output_in_en_d) begin
				o_counter <= o_counter + 1;
				if (o_counter == 7'd6) begin
					o_output_in_en <= 1;
				end else if (o_counter == 7'd7) begin
					o_output_in_en <= 0;
				end
			end else begin
				o_counter <= 0;
				o_weight_out_en <= 0;
				o_activation_out_en <= 0;
			end
			// if (output_in_en_d) begin
			// 	o_counter <= o_counter + 1;
			// 	if (o_counter == 7'd6) begin
			// 		o_output_in_en <= 1;
			// 	end else if (o_counter == 7'd7) begin
			// 		o_output_in_en <= 0;
			// 	end
			// end
		end
 	end


	// always @(posedge o_weight_out_en) begin
	// 	o_WL_address <= o_WL_address + 1;
	// 	if (o_WL_address == 9'd3) begin
	// 			o_WL_address <= 0;
	// 	end
	// end


	///////////////////////////////////////
	always @(o_WL_address) begin
		if (o_WL_address == 9'd4) begin
			o_weight_sel <= o_weight_sel + 1;
			o_WL_address <= 0;
		end
	end
	///////////////////////////////////////


endmodule


*/