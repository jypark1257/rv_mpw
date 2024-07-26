module pim_controller (
	input CLK, 
	input RSTN,

	input [31:0] i_address_bus,
	input [31:0] i_data_bus,

	input i_pim_result_out_en,

	input [31:0] i_result_buffer_out,
	
	output o_weight_in_en,
	output o_weight_out_en,
	output [15:0] o_cam_weight_in_data,
	output [15:0] o_mac_weight_in_data,

	output reg [8:0] o_WL_address,

	output o_activation_in_en,
	output o_activation_out_en,
	output [31:0] o_activation_in_data,

	output reg o_result_out_en,
	
	output [31:0] o_data_bus,

	output reg [7:0] o_counter
);

	reg result_out_en;
	reg pim_status_read;
	wire busy;
	reg valid;
	reg [8:0] WL_address_tmp;

	//counter
	always @(posedge CLK) begin
		if (!RSTN) begin
			o_counter <= 0;
		end else begin
			if (o_weight_in_en) begin 
				if (o_counter == 8'd15) begin
					o_counter  <= 0;
				end else begin
					o_counter  <= o_counter + 1;
				end
			end else if (o_activation_in_en) begin  
				if (o_counter == 8'd8) begin
					o_counter  <= 0;
				end else begin
					o_counter  <= o_counter + 1;
				end
			end else if (o_result_out_en) begin
					o_counter <= o_counter + 1;
			end	else begin
				o_counter <= 0;
			end
		end
	end

	//weight
	assign o_weight_in_en = (i_address_bus[31:4] == 28'h4000_004) ? 1 : 0;
	assign o_cam_weight_in_data = o_weight_in_en ? {i_data_bus[31:28], i_data_bus[23:20], i_data_bus[15:12], i_data_bus[7:4]} : 16'b0;
	assign o_mac_weight_in_data = o_weight_in_en ? {i_data_bus[27:24], i_data_bus[19:16], i_data_bus[11:8], i_data_bus[3:0]} : 16'b0;
	assign o_weight_out_en = (o_weight_in_en & (o_counter[3:0] == 4'd15)) ? 1 : 0;

	//WL_address 
	always @(posedge CLK) begin
		if (!RSTN) begin
			WL_address_tmp <= 0;
		end else begin
			if (o_weight_in_en) begin
				if (o_weight_out_en) begin 
					if (WL_address_tmp == 9'd287) begin
						WL_address_tmp <= 0;
					end else 
					begin
						WL_address_tmp <= WL_address_tmp + 1;
					end
				end
			end else begin
				WL_address_tmp <= 0;
			end
		end
	end

	always @(posedge CLK) begin
		if (!RSTN) begin
			o_WL_address <= 0;
		end else begin
			if (o_weight_out_en) begin
				o_WL_address <= WL_address_tmp;
			end
		end
	end

	//WL driver end
	reg WL_driver_end;
	always @(posedge CLK) begin
		if (!RSTN) begin
			WL_driver_end <= 0;
		end else begin
			if (o_weight_out_en) begin
				if (o_WL_address == 9'd287) begin
					WL_driver_end <= 1;
				end
			end else begin
				WL_driver_end <= 0;
			end
		end
	end
	
	//activation
	assign o_activation_in_en = (i_address_bus[31:4] == 28'h4000_008) ? 1 : 0;
	assign o_activation_in_data = o_activation_in_en ? i_data_bus : 32'b0;
	assign o_activation_out_en = (o_activation_in_en & (o_counter == 8'd8)) ? 1 : 0;

	//result_out_en
	always @(posedge CLK) begin
		if (!RSTN) begin
			o_result_out_en <= 0;
		end else begin
			if (i_address_bus[31:4] == 28'h4000_002) begin
				o_result_out_en <= 1;
			end else begin
				o_result_out_en <= 0;
			end
		end
	end

	//pim_status_read
	always @(posedge CLK) begin
		if (!RSTN) begin
			pim_status_read <= 0;
		end else begin
			if (i_address_bus == 32'h4000_0010) begin
				pim_status_read <= 1;
			end else begin
				pim_status_read <= 0;
			end
		end
	end
	
	//busy
	assign busy = (o_weight_in_en | o_activation_in_en | o_result_out_en) ? 1 : 0;
	
	//valid
	always @(posedge CLK) begin
		if (!RSTN) begin
			valid <= 0;
		end else begin
			if (i_pim_result_out_en) begin
				valid <= 1;
			end 
			if (o_result_out_en & (o_counter == 8'd255 )) begin
				valid <= 0;
			end
		end
	end
	
	assign o_data_bus = pim_status_read ? {30'b0, valid, busy} : (o_result_out_en ? i_result_buffer_out : 0);

endmodule

