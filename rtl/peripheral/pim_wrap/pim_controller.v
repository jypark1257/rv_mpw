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

	output o_result_buffer_busy,
	output o_result_in_en,
	output reg o_result_out_en,
	
	output reg [7:0] o_counter,
	output reg o_busy,
	output reg o_valid,
	output reg o_pim_status_read
);
	
	reg activation_in_en_d;
	wire activation_in_end;

	wire result_out_en;
	reg result_in_wait;
	reg result_buffer_busy;

	//counter
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_counter <= 0;
		end else begin
			if (o_weight_in_en) begin 
				o_counter <= o_counter + 1;
			end else if (o_activation_in_en) begin  
				if (o_counter == 8'd8) begin
					o_counter  <= 0;
				end else begin
					o_counter  <= o_counter + 1;
				end
			end else if (result_in_wait) begin
				o_counter <= o_counter + 1;
			end else if (o_result_out_en) begin
				//if (o_result_out_en) begin
					o_counter <= o_counter + 1;
				//end
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
			if (o_weight_in_en) begin 
				o_busy = 1;
			end else if (o_activation_in_en) begin 
				o_busy = 1;
			end else if (result_in_wait | activation_in_end) begin
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
			if (result_out_en) begin
				o_valid <= 0;
			end
		end
	end

	//pim_status_read
	always @(posedge i_clk) begin
		if (i_address == 32'h4000_0010) begin
			o_pim_status_read <= 1;
		end else begin
			o_pim_status_read <= 0;
		end
	end

	//o_weight_in_en signal generate & weight pim select
	always @(*) begin
		case (i_address) 
			32'h4000_0041: begin
				o_weight_in_en = 1;
				o_weight_sel = 2'b00;
			end
			32'h4000_0042: begin
				o_weight_in_en = 1;
				o_weight_sel = 2'b01;
			end
			32'h4000_0044: begin
				o_weight_in_en = 1;
				o_weight_sel = 2'b10;
			end
			32'h4000_0048: begin
				o_weight_in_en = 1;
				o_weight_sel = 2'b11;
			end
			default: begin
				o_weight_in_en = 0;
				o_weight_sel = 2'b00;
			end
		endcase
	end

	//o_weight_out_en
	always @(*) begin	
		if (i_rst) begin
			o_weight_out_en <= 0;
		end else begin
			if (o_weight_in_en) begin 
				if (o_counter[3:0] == 4'd15) begin 
					o_weight_out_en <= 1;
				end else begin
					o_weight_out_en <= 0;
				end
			end else begin
				o_weight_out_en <= 0;
			end
		end
	end

	//o_WL_address 
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_WL_address <= 0;
		end else begin
			if (o_weight_in_en) begin
				if (o_weight_out_en) begin 
					if (o_WL_address == 9'd287) begin
						o_WL_address <= 0;
					end else begin
						o_WL_address <= o_WL_address + 1;
					end
				end
			end else begin
				o_WL_address <= 0;
			end
		end
	end
	
	//activation_in_en signal generate & activation pim select
	always @(*) begin
		case (i_address) 
			32'h4000_0081: begin
				o_activation_in_en = 1;
				o_activation_sel = 2'b00;
			end
			32'h4000_0082: begin
				o_activation_in_en = 1;
				o_activation_sel = 2'b01;
			end
			32'h4000_0084: begin
				o_activation_in_en = 1;
				o_activation_sel = 2'b10;
			end
			32'h4000_0088: begin
				o_activation_in_en = 1;
				o_activation_sel = 2'b11;
			end
			default: begin
				o_activation_in_en = 0;
				o_activation_sel = 2'b00;
			end
		endcase
	end

	//o_activation_out_en
	always @(*) begin
		if (i_rst) begin
			o_activation_out_en = 0;
		end else begin
			if (o_activation_in_en) begin
				if (o_counter == 8'd8) begin
					o_activation_out_en = 1;
				end else begin
					o_activation_out_en = 0;
				end
			end	else begin
				o_activation_out_en = 0;
			end
		end
 	end

	always @(posedge i_clk) begin
		if (i_rst) begin
			activation_in_en_d <= 0;
		end else begin
			activation_in_en_d <= o_activation_in_en;
		end
	end

	assign activation_in_end = ~(o_activation_in_en | ~activation_in_en_d);

	//result_in_wait
	always @(posedge i_clk) begin
		if (i_rst) begin
			result_in_wait <= 0;
		end else begin
			if (activation_in_end) begin 
				result_in_wait <= 1;
			end else if (o_result_in_en) begin
				result_in_wait <= 0;
			end
		end
 	end

	assign o_result_in_en = (result_in_wait && (o_counter == 8'd7)) ? 1 : 0;
	assign result_out_en = (i_address[31:4] == 32'h4000_002) ? 1 : 0;
	
	always @(posedge i_clk) begin
		if (i_rst) begin
			o_result_out_en <= 0;
		end else begin
			o_result_out_en <= result_out_en;
		end
	end

	always @(posedge i_clk)	begin
		if (i_rst) begin
			result_buffer_busy <= 0;
		end else begin
			if (o_result_in_en) begin
				result_buffer_busy <= 1;
			end else if (result_out_en) begin
				result_buffer_busy <= 0;
			end
		end
	end

	assign o_result_buffer_busy = result_buffer_busy | o_result_in_en | result_out_en;

endmodule




// module pim_controller (
// 	input i_clk, 
// 	input i_rst,
// 	input [31:0] i_address,
	
// 	output o_weight_buffer_busy,
// 	output reg o_weight_in_en,
// 	output reg o_weight_out_en,
// 	output reg [1:0] o_weight_sel,
// 	output reg [8:0] o_WL_address,

// 	output o_activation_buffer_busy,
// 	output reg o_activation_in_en,
// 	output reg o_activation_out_en,
// 	output reg [1:0] o_activation_sel,

// 	output o_result_buffer_busy,
// 	output o_result_in_en,
// 	output reg o_result_out_en,
	
// 	output reg [7:0] o_counter,
// 	output reg o_busy,
// 	output reg o_valid,
// 	output reg o_pim_status_read
// );

// 	wire result_out_en_1; 
// 	wire activation_in_end;
// 	wire activation_in_en;
// 	wire result_out_en;
// 	reg weight_in_en_d, activation_in_en_d;
// 	reg result_out_en_2;
// 	reg result_in_en;
// 	reg activation_in_en_1;
// 	reg result_buffer_busy;

// 	//counter
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			o_counter <= 0;
// 		end else begin
// 			if (o_weight_buffer_busy) begin 
// 				if (o_weight_in_en) begin 
// 					o_counter <= o_counter + 1;
// 				end
// 			end else if (activation_in_en) begin 
// 				if (o_activation_in_en) begin 
// 					if (o_counter == 8'd8) begin
// 						o_counter  <= 0;
// 					end else begin
// 						o_counter  <= o_counter + 1;
// 					end
// 				end
// 			end else if (result_in_en) begin
// 				o_counter <= o_counter + 1;
// 			end else if (result_out_en) begin
// 				if (o_result_out_en) begin
// 					o_counter <= o_counter + 1;
// 				end
// 			end	else begin
// 				o_counter <= 0;
// 			end
// 		end
// 	end

// 	//busy
// 	always @(*) begin
// 		if (i_rst) begin
// 			o_busy = 0;
// 		end else begin
// 			if (o_weight_buffer_busy) begin 
// 				o_busy = 1;
// 			end else if (activation_in_en | activation_in_end) begin 
// 				o_busy = 1;
// 			end else if (result_in_en) begin
// 				o_busy = 1;
// 			end else if (result_out_en) begin
// 				o_busy = 1;
// 			end	else begin
// 				o_busy = 0;
// 			end
// 		end
// 	end
	
// 	//valid
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			o_valid <= 0;
// 		end else begin
// 			if(o_result_in_en) begin
// 				o_valid <= 1;
// 			end
// 			if (result_out_en_1) begin
// 				o_valid <= 0;
// 			end
// 		end
// 	end

// 	//PIM_control
// 	always @(posedge i_clk) begin
// 		if (i_address == 32'h4000_0010) begin
// 			o_pim_status_read <= 1;
// 		end else begin
// 			o_pim_status_read <= 0;
// 		end
// 	end

// 	//weight_in_en signal generate
// 	always @(*) begin
// 		case (i_address) 
// 			32'h4000_0041: begin
// 				o_weight_in_en = 1;
// 			end
// 			32'h4000_0042: begin
// 				o_weight_in_en = 1;
// 			end
// 			32'h4000_0044: begin
// 				o_weight_in_en = 1;
// 			end
// 			32'h4000_0048: begin
// 				o_weight_in_en = 1;
// 			end
// 			default: begin
// 				o_weight_in_en = 0;
// 			end
// 		endcase
// 	end

// 	//o_weight_out_en
// 	always @(*) begin	
// 		if (i_rst) begin
// 			o_weight_out_en <= 0;
// 		end else begin
// 			if (o_weight_buffer_busy) begin 
// 				if (o_weight_in_en) begin 
// 					if (o_counter[3:0] == 4'd15) begin 
// 						o_weight_out_en <= 1;
// 					end else begin
// 						o_weight_out_en <= 0;
// 					end
// 				end else begin
// 					o_weight_out_en <= 0;
// 				end
// 			end else begin
// 				o_weight_out_en <= 0;
// 			end
// 		end
// 	end
// 	// always @(posedge i_clk) begin
// 	// 	if (i_rst) begin
// 	// 		o_weight_out_en <= 0;
// 	// 	end else begin
// 	// 		if (o_weight_buffer_busy) begin 
// 	// 			if (o_weight_in_en) begin 
// 	// 				if (o_counter[3:0] == 4'd15) begin 
// 	// 					o_weight_out_en <= 1;
// 	// 				end else begin
// 	// 					o_weight_out_en <= 0;
// 	// 				end
// 	// 			end else begin
// 	// 				o_weight_out_en <= 0;
// 	// 			end
// 	// 		end else begin
// 	// 			o_weight_out_en <= 0;
// 	// 		end
// 	// 	end
//  	// end

// 	//weight select
// 	always @(*) begin
// 		if (i_rst) begin
// 			o_weight_sel = 0;
// 		end else begin
// 			if (o_weight_in_en) begin
// 				case (i_address) 
// 					32'h4000_0041: begin
// 						o_weight_sel = 2'b00;
// 					end
// 					32'h4000_0042: begin
// 						o_weight_sel = 2'b01;
// 					end
// 					32'h4000_0044: begin
// 						o_weight_sel = 2'b10;
// 					end
// 					32'h4000_0048: begin
// 						o_weight_sel = 2'b11;
// 					end
// 				endcase
// 			end
// 		end
// 	end

// 	//o_WL_address 
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			o_WL_address <= 0;
// 		end else begin
// 			if (o_weight_buffer_busy) begin
// 				if (o_weight_out_en) begin 
// 					if (o_WL_address == 9'd287) begin
// 						o_WL_address <= 0;
// 					end else begin
// 						o_WL_address <= o_WL_address + 1;
// 					end
// 				end
// 			end else begin
// 				o_WL_address <= 0;
// 			end
// 		end
// 	end
	
// 	//activation_in_en signal generate
// 	always @(*) begin
// 		case (i_address) 
// 			32'h4000_0081: begin
// 				o_activation_in_en = 1;
// 			end
// 			32'h4000_0082: begin
// 				o_activation_in_en = 1;
// 			end
// 			32'h4000_0084: begin
// 				o_activation_in_en = 1;
// 			end
// 			32'h4000_0088: begin
// 				o_activation_in_en = 1;
// 			end
// 			default: begin
// 				o_activation_in_en = 0;
// 			end
// 		endcase
// 	end

// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			activation_in_en_1 <= 0;
// 		end else begin
// 			activation_in_en_1 <= activation_in_en;
// 		end
// 	end

// 	assign activation_in_end = ~(activation_in_en | ~activation_in_en_1);

// 	//o_activation_out_en
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			o_activation_out_en <= 0;
// 		end else begin
// 			if (o_activation_in_en) begin
// 				if (o_counter == 8'd8) begin
// 					o_activation_out_en <= 1;
// 				end else begin
// 					o_activation_out_en <= 0;
// 				end
// 			end	else begin
// 				o_activation_out_en <= 0;
// 			end
// 		end
//  	end

// 	//activation select
// 	always @(*) begin
// 		if (i_rst) begin
// 			o_activation_sel = 0;
// 		end else begin
// 			if (o_activation_in_en) begin
// 				case (i_address) 
// 					32'h4000_0081: begin
// 						o_activation_sel = 2'b00;
// 					end
// 					32'h4000_0082: begin
// 						o_activation_sel = 2'b01;
// 					end
// 					32'h4000_0084: begin
// 						o_activation_sel = 2'b10;
// 					end
// 					32'h4000_0088: begin
// 						o_activation_sel = 2'b11;
// 					end
// 				endcase
// 			end
// 		end
// 	end

// 	//result_in_en
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			result_in_en <= 0;
// 		end else begin
// 			if (activation_in_end) begin 
// 				result_in_en <= 1;
// 			end else if (o_result_in_en) begin
// 				result_in_en <= 0;
// 			end
// 		end
//  	end

// 	assign o_result_in_en = (result_in_en && (o_counter == 8'd6)) ? 1 : 0;
// 	assign result_out_en_1 = (i_address == 32'h4000_0020) ? 1 : 0;
// 	assign activation_in_en = o_activation_in_en | activation_in_en_d;
// 	assign result_out_en = o_result_out_en | result_out_en_2;
	
// 	always @(posedge i_clk) begin
// 		if (i_rst) begin
// 			weight_in_en_d <= 0;
// 			activation_in_en_d <= 0;
// 			o_result_out_en <= 0;
// 			result_out_en_2 <= 0;
// 		end else begin
// 			weight_in_en_d <= o_weight_in_en;
// 			activation_in_en_d <= o_activation_in_en;
// 			o_result_out_en <= result_out_en_1;
// 			result_out_en_2 <= o_result_out_en;
// 		end
// 	end

// 	always @(posedge i_clk)	begin
// 		if (i_rst) begin
// 			result_buffer_busy <= 0;
// 		end else begin
// 			if (o_result_in_en) begin
// 				result_buffer_busy <= 1;
// 			end else if (result_out_en_1) begin
// 				result_buffer_busy <= 0;
// 			end
// 		end
// 	end

// 	assign o_weight_buffer_busy = o_weight_in_en | weight_in_en_d;
// 	assign o_activation_buffer_busy = activation_in_en | activation_in_end;
// 	assign o_result_buffer_busy = result_buffer_busy | o_result_in_en | result_out_en;

// endmodule



