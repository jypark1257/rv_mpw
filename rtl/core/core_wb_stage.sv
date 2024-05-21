
module core_wb_stage #(
    parameter XLEN = 32,
    parameter FLEN = 32
) (
    input           [3:0]       i_d_size,
    input                       i_d_unsigned,
    input           [2:0]       i_mem_to_reg,
    input           [XLEN-1:0]  i_data_rd_data,
    input           [XLEN-1:0]  i_imm,
    input           [XLEN-1:0]  i_pc_plus_4,
    input           [XLEN-1:0]  i_alu_result,
    output  logic   [XLEN-1:0]  o_rd_din
);
    // REGISTER SOURCE
    localparam SRC_ALU = 3'b000;
    localparam SRC_DMEM = 3'b001;
    localparam SRC_PC_PLUS_4 = 3'b010;
    localparam SRC_IMM = 3'b011;

    logic [31:0] dmem_dout;
    logic [31:0] dmem_dout_sized;
    logic [31:0] dmem_dout_byte;
    logic [31:0] dmem_dout_half;

    assign dmem_dout = i_data_rd_data;
    
    always @(*) begin
        dmem_dout_byte = '0;
        dmem_dout_half = '0;
        case (i_alu_result[1:0])
            2'b01: begin 
                dmem_dout_byte = {24'b0, dmem_dout[15:8]};
                dmem_dout_half = {16'b0, dmem_dout[23:8]};
            end
            2'b10: begin
                dmem_dout_byte = {24'b0, dmem_dout[23:16]};
                dmem_dout_half = {16'b0, dmem_dout[31:16]};
            end
            2'b11: begin
                dmem_dout_byte = {24'b0, dmem_dout[31:24]};
                //default (with strict-align, will not happen set default)
                dmem_dout_half = {16'b0, dmem_dout[15:0]};
            end
            default: begin
                dmem_dout_byte = {24'b0, dmem_dout[7:0]};
                dmem_dout_half = {16'b0, dmem_dout[15:0]};
            end
        endcase
    end


    always @(*) begin
        case (i_d_size)
            4'b0001: begin    // BYTE
                if (i_d_unsigned) begin
                    dmem_dout_sized = dmem_dout_byte;
                end else begin
                    dmem_dout_sized = $signed(dmem_dout_byte << 24) >>> 24;
                end
            end
            4'b0011: begin    // HALF WORD
                if (i_d_unsigned) begin
                    dmem_dout_sized = dmem_dout_half;
                end else begin
                    dmem_dout_sized = $signed(dmem_dout_half << 16) >>> 16;
                end
            end
            4'b1111: begin    // WORD
                dmem_dout_sized = dmem_dout;
            end
            default: begin
                dmem_dout_sized = dmem_dout;
            end
        endcase
    
    end

    always @(*) begin
        case(i_mem_to_reg)
            SRC_ALU:
                o_rd_din = i_alu_result;    // alu result
            SRC_DMEM:
                o_rd_din = dmem_dout_sized; // memory read
            SRC_PC_PLUS_4: 
                o_rd_din = i_pc_plus_4;     // pc + 4
            SRC_IMM:
                o_rd_din = i_imm;           // immediate
            default: 
                o_rd_din = i_alu_result;
        endcase 
    end

endmodule