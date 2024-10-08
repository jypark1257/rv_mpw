`include "/home/pjy-wsl/rv_cores/rv_mpw/rtl/headers/opcode.svh"

module immediate_generator (
    input           [6:0]   i_opcode,
    input           [4:0]   i_rd,
    input           [2:0]   i_funct3,
    input           [4:0]   i_rs1,
    input           [4:0]   i_rs2,
    input           [6:0]   i_funct7,
    output  logic   [31:0]  o_imm
);

    // SHIFTS
    localparam FUNCT3_SL = 3'b001;
    localparam FUNCT3_SR = 3'b101;

    logic [11:0] imm_i;     // immediate
    logic [11:0] imm_s;     // store
    logic [12:0] imm_b;     // branch
    logic [20:0] imm_j;     // jump
    logic [4:0]  sht_amt;   // shift amount
    logic [19:0] imm_u;     //upper immediate

    logic [31:0] imm_pim_sext;
    logic [31:0] imm_i_sext;
    logic [31:0] imm_s_sext;
    logic [31:0] imm_b_sext;
    logic [31:0] sht_amt_sext;
    logic [31:0] imm_j_sext;
    logic [31:0] imm_u_zfill;

    // Immediate parsing
    assign imm_i = {i_funct7, i_rs2};
    assign imm_s = {i_funct7, i_rd};
    assign imm_b = {i_funct7[6], i_rd[0], i_funct7[5:0], i_rd[4:1], 1'b0};
    assign imm_j = {i_funct7[6], i_rs1, i_funct3, i_rs2[0], i_funct7[5:0], i_rs2[4:1], 1'b0};
    assign sht_amt = i_rs2;
    assign imm_u = {i_funct7, i_rs2, i_rs1, i_funct3};
    

    // Extension
    assign imm_i_sext = {{20{imm_i[11]}}, imm_i};
    assign imm_s_sext = {{20{imm_s[11]}}, imm_s};
    assign imm_b_sext = {{19{imm_b[12]}}, imm_b};
    assign sht_amt_sext = {{27{1'b0}}, sht_amt};
    assign imm_j_sext = {{11{imm_j[20]}}, imm_j};
    assign imm_u_zfill = {imm_u, 12'b0};
    assign imm_pim_sext = imm_s_sext;

    always_comb begin
        o_imm = '0;

        case (i_opcode)
            `OPCODE_I: begin
                if ((i_funct3 == FUNCT3_SL) || (i_funct3 == FUNCT3_SR)) begin
                    o_imm = sht_amt_sext;
                end else begin
                    o_imm = imm_i_sext;
                end
            end
            `OPCODE_STORE: begin
                o_imm = imm_s_sext;
            end
            `OPCODE_LOAD: begin
                o_imm  = imm_i_sext;
            end 
            `OPCODE_BRANCH: begin
                o_imm = imm_b_sext;
            end
            `OPCODE_JALR: begin
                o_imm = imm_i_sext;         // later, PC = rs1 + imm_i_sext
            end 
            `OPCODE_JAL: begin
                o_imm = imm_j_sext;         // later, PC = PC + imm_i_sext
            end
            `OPCODE_AUIPC: begin
                o_imm = imm_u_zfill;        // later, rd = PC + imm_u_zfill
            end
            `OPCODE_LUI: begin
                o_imm = imm_u_zfill;
            end
            `OPCODE_PIM: begin
                o_imm = imm_pim_sext;
            end
            default: 
                o_imm = '0;
        endcase
    end

endmodule
