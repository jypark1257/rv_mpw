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
    output logic    [31:0]  o_imem_dout,

    // SPI SLAVE
    input                   i_req_spi,
    output                  o_gnt_spi,
    input           [31:0]  i_spi_addr,
    input                   i_spi_write,
    input                   i_spi_read,
    input           [ 3:0]  i_spi_size,
    input           [31:0]  i_spi_din,
    output logic    [31:0]  o_spi_dout,

    // RV DMEM
    input                   i_req_dmem,
    output                  o_gnt_dmem,
    input           [31:0]  i_dmem_addr,
    input                   i_dmem_write,
    input                   i_dmem_read,
    input           [ 3:0]  i_dmem_size,
    input           [31:0]  i_dmem_din,
    output logic    [31:0]  o_dmem_dout,

    // DMA
    input                   i_req_dma,
    output                  o_gnt_dma,
    input           [31:0]  i_dma_addr,
    input                   i_dma_write,
    input                   i_dma_read,
    input           [ 3:0]  i_dma_size,
    input           [31:0]  i_dma_din,
    output logic    [31:0]  o_dma_dout,

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
    input           [31:0]  i_dmem_dout,

    // PIM BUFFER SRAM
    output logic    [31:0]  o_buf_addr,
    output logic            o_buf_write,
    output logic            o_buf_read,
    output logic    [ 3:0]  o_buf_size,
    output logic    [31:0]  o_buf_din,
    input           [31:0]  i_buf_dout,

    // UART
    output logic    [31:0]  o_uart_addr,
    output logic            o_uart_write,
    output logic            o_uart_read,
    output logic    [ 3:0]  o_uart_size,
    output logic    [31:0]  o_uart_din,
    input           [31:0]  i_uart_dout,

    // Hybrid-PIM
    output logic    [31:0]  o_pim_addr,
    output logic            o_pim_write,
    output logic            o_pim_read,
    output logic    [ 3:0]  o_pim_size,
    output logic    [31:0]  o_pim_din,
    input           [31:0]  i_pim_dout
);    

    // latch dmem address
    logic [31:0] dmem_addr_q;
    logic [31:0] dma_addr_q;

    // internal grant signal 
    logic gnt_imem;

    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
            dmem_addr_q <= '0;
            dma_addr_q <= '0;
        end else begin
            dmem_addr_q <= i_dmem_addr;
            dma_addr_q <= i_dma_addr;
        end
    end

    // priority arbiter
    ids_arbiter arbiter (
        .i_clk      (i_clk),
        .i_rst_n    (i_rst_n),

        .i_req_spi  (i_req_spi),
        .o_gnt_spi  (o_gnt_spi),

        .i_req_dmem (i_req_dmem),
        .o_gnt_dmem (o_gnt_dmem),

        .i_req_dma  (i_req_dma),
        .o_gnt_dma  (o_gnt_dma)
    );

    assign gnt_imem = !(o_gnt_spi && (i_spi_addr[31:12] == 20'h40000));


    // SLAVE IMEM PORT
    assign o_imem_addr  = (gnt_imem) ? i_imem_addr : i_spi_addr;
    assign o_imem_read  = (gnt_imem) ? i_imem_read : i_spi_read;
    assign o_imem_write = (gnt_imem) ? i_imem_write : i_spi_write;
    assign o_imem_size  = (gnt_imem) ? i_imem_size : i_spi_size;
    assign o_imem_din   = (gnt_imem) ? i_imem_din : i_spi_din;

    // SLAVE DMEM PORT
    always @(*) begin
        o_dmem_addr = '0;
        o_dmem_write = '0;
        o_dmem_read = '0;
        o_dmem_size = '0;
        o_dmem_din = '0;
        o_uart_addr = '0;
        o_uart_write = '0;
        o_uart_read = '0;
        o_uart_size = '0;
        o_uart_din = '0;
        o_buf_addr = '0;
        o_buf_write = '0;
        o_buf_read = '0;
        o_buf_size = '0;
        o_buf_din = '0;
        o_pim_addr = '0;
        o_pim_write = '0;
        o_pim_read = '0;
        o_pim_size = '0;
        o_pim_din = '0;
        case ({o_gnt_spi, o_gnt_dmem, o_gnt_dma})
            3'b100: begin   // SPI GRANTED
                case (i_spi_addr[31:28])
                    4'h2: begin // SPI ACCESS PIM_BUFFER
                        o_buf_addr = i_spi_addr;
                        o_buf_write = i_spi_write;
                        o_buf_read = i_spi_read;
                        o_buf_size = i_spi_size;
                        o_buf_din = i_spi_din;
                    end
                    4'h4: begin // SPI ACCESS DMEM
                        o_dmem_addr = i_spi_addr;
                        o_dmem_write = i_spi_write;
                        o_dmem_read = i_spi_read;
                        o_dmem_size = i_spi_size;
                        o_dmem_din = i_spi_din;
                    end
                    default: begin
                        o_dmem_addr = i_spi_addr;
                        o_dmem_write = i_spi_write;
                        o_dmem_read = i_spi_read;
                        o_dmem_size = i_spi_size;
                        o_dmem_din = i_spi_din;
                    end
                endcase
            end
            3'b010: begin    // DMEM GRANTED
                case (i_dmem_addr[31:28])
                    4'h2: begin // RV_DMEM ACCESS PIM_BUFFER
                        o_buf_addr = i_dmem_addr;
                        o_buf_write = i_dmem_write;
                        o_buf_read = i_dmem_read;
                        o_buf_size = i_dmem_size;
                        o_buf_din = i_dmem_din;
                    end
                    4'h4: begin // RV_DMEM ACCESS DMEM
                        o_dmem_addr = i_dmem_addr;
                        o_dmem_write = i_dmem_write;
                        o_dmem_read = i_dmem_read;
                        o_dmem_size = i_dmem_size;
                        o_dmem_din = i_dmem_din;
                    end
                    4'h8: begin // RV_DMEM ACCESS UART
                        o_uart_addr = i_dmem_addr;
                        o_uart_write = i_dmem_write;
                        o_uart_read = i_dmem_read;
                        o_uart_size = i_dmem_size;
                        o_uart_din = i_dmem_din;
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
            3'b001: begin    // DMA GRANTED
                case (i_dma_addr[31:28])
                    4'h2: begin // DMA ACCESS PIM_BUFFER
                        o_buf_addr = i_dma_addr;
                        o_buf_write = i_dma_write;
                        o_buf_read = i_dma_read;
                        o_buf_size = i_dma_size;
                        o_buf_din = i_dma_din;
                    end
                    4'h4: begin // DMA ACCESS DMEM
                        o_pim_addr = i_dma_addr;
                        o_pim_write = i_dma_write;
                        o_pim_read = i_dma_read;
                        o_pim_size = i_dma_size;
                        o_pim_din = i_dma_din;
                    end
                    default: begin
                        o_buf_addr = i_dma_addr;
                        o_buf_write = i_dma_write;
                        o_buf_read = i_dma_read;
                        o_buf_size = i_dma_size;
                        o_buf_din = i_dma_din;
                    end
                endcase
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
    
    // SPI SLAVE, assign zero output
    assign o_spi_dout = '0;

    // MASTER RV IMEM PORT
    assign o_imem_dout = i_imem_dout;

    // MASTER RV DMEM PORT
    always @(*) begin
        case (dmem_addr_q[31:28])
            4'h0: begin // DMEM ACCESS
                o_dmem_dout = i_dmem_dout;
            end
            4'h2: begin // PIM_BUFFER ACCESS
                o_dmem_dout = i_buf_dout;
            end
            4'h8: begin // UART ACCESS
                o_dmem_dout = i_uart_dout;
            end
            default: begin
                o_dmem_dout = i_dmem_dout;
            end
        endcase
    end
    
    // MASTER RV DMA PORT
    always @(*) begin
        case (dma_addr_q[31:28])
            4'h2: begin // BUFFER ACCESS
                o_dma_dout = i_buf_dout;
            end
            4'h4: begin // PIM ACCESS
                o_dma_dout = i_pim_dout;
            end
            default: begin
                o_dma_dout = i_buf_dout;
            end
        endcase
    end
endmodule