`include "/home/pjy-wsl/idslab-cores/ids_mpw/rtl/headers/opcode.svh"

module alu_control_unit (
    input           [6:0]   i_opcode,
    input           [6:0]   i_funct7,
    input           [2:0]   i_funct3,
    output  logic   [4:0]   o_alu_control
);

    // ALU controls
    localparam ALU_ADD = 5'b0_0000;
    localparam ALU_AND = 5'b0_0001;
    localparam ALU_OR = 5'b0_0010;
    localparam ALU_XOR = 5'b0_0011;
    localparam ALU_SLL = 5'b0_0100;
    localparam ALU_SRL = 5'b0_0101;
    localparam ALU_SRA = 5'b0_0110;
    localparam ALU_SUB = 5'b1_0000;
    localparam ALU_SLTU = 5'b1_1000;
    localparam ALU_SLT = 5'b1_0111;

    always_comb begin
        if (i_opcode == `OPCODE_BRANCH) begin
            case (i_funct3)
                `BRANCH_BEQ: begin
                    o_alu_control = ALU_SUB;
                end
                `BRANCH_BNE: begin
                    o_alu_control = ALU_SUB;
                end
                `BRANCH_BLT: begin
                    o_alu_control = ALU_SLT;
                end
                `BRANCH_BGE: begin
                    o_alu_control = ALU_SLT;
                end
                `BRANCH_BLTU: begin
                    o_alu_control = ALU_SLTU;
                end
                `BRANCH_BGEU: begin
                    o_alu_control = ALU_SLTU;
                end
                default: begin
                    o_alu_control = ALU_SUB;
                end
            endcase
        end else if ((i_opcode == `OPCODE_R) || (i_opcode == `OPCODE_I)) begin
            case (i_funct3)
                `FUNCT3_ADD_SUB: begin
                    if (i_opcode == `OPCODE_R) begin
                        if (i_funct7 == 7'h20) begin            // `FUNCT3_SUB
                            o_alu_control = ALU_SUB;
                        end else if (i_funct7 == 7'h00) begin   // `FUNCT3_ADD
                            o_alu_control = ALU_ADD;
                        end else begin
                            o_alu_control = ALU_ADD;
                        end
                    end else begin
                        o_alu_control = ALU_ADD;                // `OPCODE_I
                    end
                end
                `FUNCT3_SLL: begin
                    o_alu_control = ALU_SLL;
                end
                `FUNCT3_SLT: begin
                    o_alu_control = ALU_SLT;
                end
                `FUNCT3_SLTU: begin
                    o_alu_control = ALU_SLTU;
                end
                `FUNCT3_XOR: begin
                    o_alu_control = ALU_XOR;
                end
                `FUNCT3_SRL_SRA: begin
                    if (i_funct7 == 7'h00) begin            // `FUNCT3_SRL
                        o_alu_control = ALU_SRL;
                    end else if (i_funct7 == 7'h20) begin   // `FUNCT3_SRA
                        o_alu_control = ALU_SRA;
                    end else begin
                        o_alu_control = ALU_ADD;
                    end
                end
                `FUNCT3_OR: begin
                    o_alu_control = ALU_OR;
                end
                `FUNCT3_AND: begin
                    o_alu_control = ALU_AND;
                end 
                default: begin
                    o_alu_control = ALU_ADD;
                end
            endcase
        end else begin
            o_alu_control = ALU_ADD;                    // set default to ADD operation, for LOAD, STORE, JAL(R), and AUIPC
        end
    end

endmodule