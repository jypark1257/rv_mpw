module main_control_unit (
    input           [6:0]   i_opcode,
    input           [4:0]   i_rd,
    input           [2:0]   i_funct3,
    input           [4:0]   i_rs1,
    input           [6:0]   i_funct7,
    // Regiser File control 
    output  logic           o_reg_write,
    // DMEM Read/Write Control
    output  logic   [3:0]   o_d_size,
    output  logic           o_d_unsigned,
    output  logic   [2:0]   o_mem_to_reg,
    output  logic           o_mem_read,
    output  logic           o_mem_write
);



    // SIZES
    localparam SIZE_HALF = 2'b01;
    localparam SIZE_WORD = 2'b10;

    // REGISTER SOURCE
    localparam SRC_ALU = 3'b000;
    localparam SRC_DMEM = 3'b001;
    localparam SRC_PC_PLUS_4 = 3'b010;
    localparam SRC_IMM = 3'b011;

    always_comb begin
        o_mem_read = '0;
        o_mem_write = '0;
        o_reg_write = '0;
        o_d_size = '0;
        o_d_unsigned = '0;
        o_mem_to_reg = '0;
        case (i_opcode)
            OPCODE_R: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_ALU;         // arithmetic instructions
            end
            OPCODE_I: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_ALU;
            end
            OPCODE_STORE: begin
                o_mem_write = 1'b1;
                case (i_funct3)
                    FUNCT3_BYTE: begin
                        o_d_size = 4'b0001;
                    end
                    FUNCT3_HALF: begin
                        o_d_size = 4'b0011;
                    end
                    FUNCT3_WORD: begin
                        o_d_size = 4'b1111;
                    end
                    default: begin
                        o_d_size = '0;
                    end
                endcase
            end
            OPCODE_LOAD: begin
                o_mem_read = 1'b1;
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_DMEM;
                case (i_funct3)
                    FUNCT3_BYTE: begin
                        o_d_size = 4'b0001;
                    end
                    FUNCT3_HALF: begin
                        o_d_size = 4'b0011;
                    end
                    FUNCT3_WORD: begin
                        o_d_size = 4'b1111;
                    end
                    FUNCT3_BYTE_U: begin
                        o_d_size = 4'b0001;
                        o_d_unsigned = 1'b1;
                    end
                    FUNCT3_HALF_U: begin
                        o_d_size = 4'b0011;
                        o_d_unsigned = 1'b1;
                    end 
                    default: begin
                        o_d_size = '0;
                        o_d_unsigned = '0;
                    end
                endcase
            end
            OPCODE_JALR: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_PC_PLUS_4;
            end
            OPCODE_JAL: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_PC_PLUS_4;
            end
            OPCODE_AUIPC: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_ALU;
            end
            OPCODE_LUI: begin
                o_reg_write = 1'b1;
                o_mem_to_reg = SRC_IMM;
            end
            default: begin
                o_mem_read = '0;
                o_mem_write = '0;
                o_reg_write = '0;
                o_d_size = '0;
                o_d_unsigned = '0;
                o_mem_to_reg = '0;
            end
        endcase
    end

endmodule