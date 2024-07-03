`include "/home/pjy-wsl/idslab-cores/ids_mpw/rtl/headers/opcode.svh"

module branch_unit #(
    parameter XLEN = 32
) (
    input           [6:0]       i_opcode,
    input           [2:0]       i_funct3,
    input                       i_alu_zero,
    input           [XLEN-1:0]  i_pc,
    input           [31:0]      i_rs1_dout,
    input           [31:0]      i_imm,
    output  logic               o_branch_taken,
    output  logic   [XLEN-1:0]  o_pc_branch
);


    always_comb begin
        o_branch_taken = '0;
        o_pc_branch = '0;

        case (i_opcode)
            `OPCODE_JAL: begin
                o_branch_taken = 1'b1;
                o_pc_branch = i_pc + i_imm;
            end
            `OPCODE_JALR: begin
                if (i_funct3 == 3'h0) begin
                    o_branch_taken = 1'b1;
                    o_pc_branch = i_rs1_dout + i_imm;
                end else begin
                    o_branch_taken = 1'b0;
                    // invalid branch pc
                end
            end
            `OPCODE_BRANCH: begin
                o_pc_branch = i_pc + i_imm;
                case (i_funct3)
                    `BRANCH_BEQ: begin
                        o_branch_taken = (i_alu_zero) ? 1'b1 : 1'b0;
                    end
                    `BRANCH_BNE: begin
                        o_branch_taken = (!i_alu_zero) ? 1'b1 : 1'b0;
                    end
                    `BRANCH_BLT: begin
                        o_branch_taken = (!i_alu_zero) ? 1'b1 : 1'b0;
                    end
                    `BRANCH_BGE: begin
                        o_branch_taken = (i_alu_zero) ? 1'b1 : 1'b0;
                    end
                    `BRANCH_BLTU: begin
                        o_branch_taken = (!i_alu_zero) ? 1'b1 : 1'b0;
                    end
                    `BRANCH_BGEU: begin
                        o_branch_taken = (i_alu_zero) ? 1'b1 : 1'b0;
                    end 
                    default: begin
                        o_branch_taken = 1'b0;
                    end
                endcase
            end 
            default: begin
                o_branch_taken = 1'b0;
            end
        endcase
    end

endmodule
