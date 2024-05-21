/*
  Author: Jiyong Park.
  Affiliation: IDS Lab, Korea University EE.
  Description: Bus for DMEM side of core with priority arbiter.
  priority: 1. RISC-V core (IMEM) && (DMEM)
            2. DMA
*/

module ids_bus (
    input                   i_clk, 
    input                   i_rst_n,

    // RV IMEM
    input           [31:0]  i_imem_addr,
    input                   i_imem_write,
    input                   i_imem_read,
    input           [ 3:0]  i_imem_size,
    input           [31:0]  i_imem_din,
    output          [31:0]  o_imem_dout,

    // RV DMEM
    input                   i_req_dmem,
    output                  o_gnt_dmem,
    input           [31:0]  i_dmem_addr,
    input                   i_dmem_write,
    input                   i_dmem_read,
    input           [ 3:0]  i_dmem_size,
    input           [31:0]  i_dmem_din,
    output          [31:0]  o_dmem_dout,

    // DMA
    input                   i_req_dma,
    output                  o_gnt_dma,
    input           [31:0]  i_dma_addr,
    input                   i_dma_write,
    input                   i_dma_read,
    input           [ 3:0]  i_dma_size,
    input           [31:0]  i_dma_din,
    output          [31:0]  o_dma_dout,

    // IMEM SRAM (IMEM port)
    output logic    [31:0]  o_imem_addr,
    output logic            o_imem_write,
    output logic            o_imem_read,
    output logic    [ 3:0]  o_imem_size,
    output logic    [31:0]  o_imem_din,
    input           [31:0]  i_imem_dout,

    // DMEM SRAM (DMEM port)
    output logic    [31:0]  o_dmem_addr,
    output logic            o_dmem_write,
    output logic            o_dmem_read,
    output logic    [ 3:0]  o_dmem_size,
    output logic    [31:0]  o_dmem_din,
    input           [31:0]  i_dmem_dout

    // Hybrid-PIM
    // ?
);
    // priority arbiter
    ids_arbiter arbiter (
        .i_clk      (i_clk),
        .i_rst_n    (i_rst_n),

        .i_req_dmem (i_req_dmem),
        .o_gnt_dmem (o_gnt_dmem),

        .i_req_dma  (i_req_dma),
        .o_gnt_dma  (o_gnt_dma)
    );

    // SLAVE IMEM PORT
    assign o_imem_addr = i_imem_addr;
    assign o_imem_read = i_imem_read;
    assign o_imem_write = i_imem_write;
    assign o_imem_size = i_imem_size;
    assign o_imem_din = i_imem_din;

    // SLAVE DMEM PORT
    always_comb begin
        case ({o_gnt_dmem, o_gnt_dma})
            2'b10: begin    // DMEM GRANT
                o_dmem_addr = i_dmem_addr;
                o_dmem_write = i_dmem_write;
                o_dmem_read = i_dmem_read;
                o_dmem_size = i_dmem_size;
                o_dmem_din = i_dmem_din;
            end
            2'b01: begin    // DMA GRANT
                o_dmem_addr = i_dma_addr;
                o_dmem_write = 1'b0;
                o_dmem_read = 1'b0;
                o_dmem_size = i_dma_size;
                o_dmem_din = i_dma_din;
            end 
            default: begin
                o_dmem_addr = i_dmem_addr;
                o_dmem_write = i_dmem_write;
                o_dmem_read = i_dmem_read;
                o_dmem_size = i_dmem_size;
                o_dmem_din = i_dmem_din;
            end
        endcase
    end
    
    // MASTER RV IMEM PORT
    assign o_imem_dout = i_imem_dout;

    // MASTER RV DMEM PORT
    assign o_dmem_dout = i_dmem_dout;
    
    // MASTER RV DMA PORT
    assign o_dma_dout = i_dmem_dout;

endmodule