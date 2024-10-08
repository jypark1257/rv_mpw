`include "/home/pjy-wsl/rv_cores/rv_mpw/rtl/headers/opcode.svh"
//`include "/home/pjy-wsl/idslab-cores/ids_mpw/rtl/headers/pipe_reg.svh"

module core #(
    parameter XLEN = 32,
    parameter FLEN = 32,
    parameter RESET_PC = 32'h1000_0000

) (
    input                       i_clk,
    input                       i_rst_n,
    // instruction interface
    output  logic   [XLEN-1:0]  o_instr_addr,
    input           [XLEN-1:0]  i_instr_rd_data,
    output  logic   [XLEN-1:0]  o_instr_wr_data,
    output  logic   [3:0]       o_instr_size,
    output  logic               o_instr_read,
    output  logic               o_instr_write,
    // data interface
    output  logic               o_req_dmem,
    input                       i_gnt_dmem,
    output  logic   [XLEN-1:0]  o_data_addr,
    input           [XLEN-1:0]  i_data_rd_data,
    output  logic   [XLEN-1:0]  o_data_wr_data,
    output  logic   [3:0]       o_data_size,
    output  logic               o_data_read,
    output  logic               o_data_write,
    // DMA status
    input                       i_dma_busy,
    // DMA interface
    output  logic               o_dma_en,
    output  logic   [2:0]       o_dma_funct3,
    output  logic   [3:0]       o_dma_sel_pim,  
    output  logic   [12:0]      o_dma_size,
    output  logic   [31:0]      o_dma_mem_addr

);

    // pipline registers
    pipe_if_id      id;
    pipe_id_ex      ex;
    pipe_ex_wb      wb;

    logic pc_write;
    logic [XLEN-1:0] pc_curr;
    logic [XLEN-1:0] pc_instr;

    logic branch_taken;
    logic [XLEN-1:0] pc_branch;
    
    logic [6:0] opcode;
    logic [4:0] rd;
    logic [2:0] funct3;
    logic [4:0] rs1;
    logic [4:0] rs2;
    logic [6:0] funct7;

    // DMA control signals
    logic dma_en;

    logic mem_read;
    logic mem_write;
    logic reg_write;
    logic [2:0] mem_to_reg;
    logic [3:0] d_size;
    logic d_unsigned;

    logic [XLEN-1:0] wr_data;
    logic [XLEN-1:0] forward_in1;
    logic [XLEN-1:0] forward_in2;
    logic [XLEN-1:0] alu_result;
    logic ex_mem_write;

    logic [XLEN-1:0] imm;

    logic [XLEN-1:0] rs1_dout;
    logic [XLEN-1:0] rs2_dout;

    logic [XLEN-1:0] rd_din;
    
    logic stall;
    logic if_flush;    
    logic id_flush;
    logic if_stall;


    // --------------------------------------------------------

    core_if_stage #(
        .XLEN(32),
        .RESET_PC(RESET_PC)
    ) core_IF (
        .i_clk          (i_clk),
        .i_rst_n        (i_rst_n),
        .i_pc_write     (pc_write),
        .i_branch_taken (branch_taken),
        .i_pc_branch    (pc_branch),
        .o_pc_curr      (pc_curr),
        .o_pc_instr     (pc_instr)
    );

    // Instruction memory
    logic [XLEN-1:0] instr;
    assign pc_write = (stall == 1'b0) ? 1'b1 : 1'b0;

    // instruction memory interface
    assign o_instr_addr = (branch_taken) ? pc_branch : pc_curr;
    assign instr = i_instr_rd_data;
    assign o_instr_wr_data = '0;
    assign o_instr_size = 4'b1111;        // always 32-bit access
    assign o_instr_read = (stall == 1'b0) ? 1'b1 : 1'b0;
    assign o_instr_write = 1'b0;



    // --------------------------------------------------------

    assign if_flush = (branch_taken) ? 1'b1 : 1'b0;
    assign if_stall = (stall) ? 1'b1: 1'b0;

    // IF/ID pipeline register
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            id <= '0;
        end else begin
            if (if_flush) begin
                id <= '0;
            end else if (if_stall) begin
                id.pc <= id.pc;
                id.instr <= id.instr;
            end else begin
                id.pc <= pc_instr;
                id.instr <= instr;
            end
        end
    end

    // --------------------------------------------------------

    core_id_stage #(
        .XLEN(32)
    ) core_ID (
        .i_clk          (i_clk),
        .i_rst_n        (i_rst_n),
        .i_instr        (id.instr),
        .i_rd_din       (rd_din),
        .i_wb_rd        (wb.rd),
        .i_wb_reg_write (wb.reg_write),
        .o_opcode       (opcode),
        .o_rd           (rd),
        .o_funct3       (funct3),
        .o_rs1          (rs1),
        .o_rs2          (rs2),
        .o_funct7       (funct7),
        .o_imm          (imm),
        .o_mem_read     (mem_read),
        .o_mem_write    (mem_write),
        .o_reg_write    (reg_write),
        .o_mem_to_reg   (mem_to_reg),
        .o_d_size       (d_size),
        .o_d_unsigned   (d_unsigned),
        .o_dma_en       (dma_en),
        .o_rs1_dout     (rs1_dout),
        .o_rs2_dout     (rs2_dout)
    );


    // --------------------------------------------------------

    // request for dmem use
    assign o_req_dmem = ((mem_read || mem_write) && (stall == 1'b0));
    

    // --------------------------------------------------------
    assign id_flush = (branch_taken || stall) ? 1 : 0;

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            ex <= '0;
        end else begin
            if (id_flush) begin
                ex <= '0;
            end else begin
                ex.pc <= id.pc;
                ex.opcode <= opcode;
                ex.rd <= rd;
                ex.funct3 <= funct3;
                ex.rs1 <= rs1;
                ex.rs2 <= rs2;
                ex.funct7 <= funct7;
                ex.imm <= imm;
                ex.mem_read <= mem_read;
                ex.mem_write <= mem_write;
                ex.reg_write <= reg_write;
                ex.mem_to_reg <= mem_to_reg;
                ex.d_size <= d_size;
                ex.d_unsigned <= d_unsigned;
                ex.dma_en <= dma_en;
                ex.rs1_dout <= rs1_dout;
                ex.rs2_dout <= rs2_dout;
            end
        end
    end

    // --------------------------------------------------------

    core_ex_stage #(
        .XLEN(32)
    ) core_EX (
        .i_clk          (i_clk),
        .i_rst_n        (i_rst_n),
        .i_pc           (ex.pc),
        .i_opcode       (ex.opcode),
        .i_rd           (ex.rd),
        .i_funct3       (ex.funct3),
        .i_rs1          (ex.rs1),
        .i_rs2          (ex.rs2),
        .i_funct7       (ex.funct7),
        .i_rs1_dout     (ex.rs1_dout),
        .i_rs2_dout     (ex.rs2_dout),
        .i_imm          (ex.imm),
        .i_rd_din       (rd_din),
        .i_wb_rd        (wb.rd),
        .i_wb_reg_write (wb.reg_write),
        .o_alu_result   (alu_result),
        .o_branch_taken (branch_taken),
        .o_pc_branch    (pc_branch),
        .o_forward_in1  (forward_in1),
        .o_forward_in2  (forward_in2)
    );

    assign stall = (i_dma_busy || ex.dma_en);


    // DMA interface
    assign o_dma_en = ex.dma_en;
    assign o_dma_funct3 = ex.funct3;
    assign o_dma_sel_pim = ex.imm[3:0];
    assign o_dma_size = forward_in1[12:0];
    assign o_dma_mem_addr = forward_in2;
    

    // data interface set
    // un-aligned store
    always @(*) begin
        wr_data = '0;
        o_data_size = '0;
        case (alu_result[1:0])
            2'b01: begin    // 
                wr_data = forward_in2 << 8;
                o_data_size = ex.d_size << 1;
            end
            2'b10: begin    // 
                wr_data = forward_in2 << 16;
                o_data_size = ex.d_size << 2;
            end
            2'b11: begin    // 
                wr_data = forward_in2 << 24;
                o_data_size = ex.d_size << 3;
            end 
            default: begin    // 
                wr_data = forward_in2;
                o_data_size = ex.d_size;
            end
        endcase
    end
    assign o_data_addr = alu_result;
    assign o_data_wr_data = wr_data;
    assign o_data_read = ex.mem_read;
    assign o_data_write = ex.mem_write;

    // --------------------------------------------------------

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            wb <= '0;
        end else begin
            wb.pc_plus_4 <= ex.pc + 4;
            wb.rd <= ex.rd;
            wb.imm <= ex.imm;
            wb.alu_result <= alu_result;
            wb.reg_write <= ex.reg_write;
            wb.mem_to_reg <= ex.mem_to_reg;
            wb.d_size <= ex.d_size;
            wb.d_unsigned <= ex.d_unsigned;
        end
    end

    // --------------------------------------------------------

    core_wb_stage #(
        .XLEN(32)
    ) core_WB (
        .i_d_size       (wb.d_size),
        .i_d_unsigned   (wb.d_unsigned),
        .i_mem_to_reg   (wb.mem_to_reg),
        .i_data_rd_data (i_data_rd_data),
        .i_imm          (wb.imm),
        .i_pc_plus_4    (wb.pc_plus_4),
        .i_alu_result   (wb.alu_result),
        .o_rd_din       (rd_din)
    );

    // --------------------------------------------------------

endmodule
