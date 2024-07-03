
module core_top #(
    parameter XLEN              = 32,
    parameter CPU_CLOCK_FREQ    = 250_000_000,
    parameter RESET_PC          = 32'h4000_0000,
    parameter BAUD_RATE         = 115200
) (
    input                       i_clk,
    // CORE RESET
    input                       i_rv_rst_n,
    
    // SPI RESET
    input                       i_spi_rst_n,

    // SPI
    input                       i_sclk,
    input                       i_cs,
    input                       i_mosi,
    output logic                o_miso,

    // UART
    input                       i_serial_rx,
    output logic                o_serial_tx,

    // PIM I/F
    output logic    [XLEN-1:0]  o_pim_addr,
    output logic    [XLEN-1:0]  o_pim_wr_data,
    input           [XLEN-1:0]  i_pim_rd_data
);

    logic                       rv_rst_n;
    logic                       bus_rst_n;


    // SPI I/F
    logic                       req_spi;
    logic                       gnt_spi;
    logic [XLEN-1:0]            spi_addr;
    logic [XLEN-1:0]            spi_rd_data;
    logic [XLEN-1:0]            spi_wr_data;
    logic [3:0]                 spi_size;
    logic                       spi_read;
    logic                       spi_write;

    // RV IMEM I/F
    logic [XLEN-1:0]            instr_addr;
    logic [XLEN-1:0]            instr_rd_data;
    logic [XLEN-1:0]            instr_wr_data;
    logic [3:0]                 instr_size;
    logic                       instr_read;
    logic                       instr_write;

    // RV DMEM I/F
    logic                       req_data;
    logic                       gnt_data;
    logic [XLEN-1:0]            data_addr;
    logic [XLEN-1:0]            data_rd_data;
    logic [XLEN-1:0]            data_wr_data;
    logic [3:0]                 data_size;
    logic                       data_read;
    logic                       data_write;

    // SRAM IMEM I/F
    logic [XLEN-1:0]            imem_addr;
    logic [XLEN-1:0]            imem_rd_data;
    logic [XLEN-1:0]            imem_wr_data;
    logic [3:0]                 imem_size;
    logic                       imem_read;
    logic                       imem_write;

    // SRAM DMEM I/F
    logic [XLEN-1:0]            dmem_addr;
    logic [XLEN-1:0]            dmem_rd_data;
    logic [XLEN-1:0]            dmem_wr_data;
    logic [3:0]                 dmem_size;  
    logic                       dmem_read;
    logic                       dmem_write;

    // PIM BUFFER I/F
    logic [XLEN-1:0]            buf_addr;
    logic [XLEN-1:0]            buf_rd_data;
    logic [XLEN-1:0]            buf_wr_data;
    logic [3:0]                 buf_size;  
    logic                       buf_read;
    logic                       buf_write;
    
    // UART
    logic [XLEN-1:0]            uart_addr;
    logic [XLEN-1:0]            uart_rd_data;
    logic [XLEN-1:0]            uart_wr_data;
    logic [3:0]                 uart_size;  
    logic                       uart_read;
    logic                       uart_write;

    // PIM BUFFER I/F
    logic [XLEN-1:0]            pim_addr;
    logic [XLEN-1:0]            pim_rd_data;
    logic [XLEN-1:0]            pim_wr_data;
    logic [3:0]                 pim_size;  
    logic                       pim_read;
    logic                       pim_write;

    // DMA
    logic                       dma_en;
    logic                       req_dma;
    logic                       gnt_dma;
    logic [2:0]                 dma_funct3;
    logic [3:0]                 dma_sel_pim;
    logic [12:0]                dma_trans_size;
    logic [XLEN-1:0]            dma_mem_addr;
    logic [XLEN-1:0]            dma_addr;
    logic                       dma_write;
    logic                       dma_read;
    logic [3:0]                 dma_size;  
    logic [XLEN-1:0]            dma_rd_data;
    logic [XLEN-1:0]            dma_wr_data;
    logic                       dma_busy;
    
    // RISC-V rst_n
    //assign rv_rst_n = (i_spi_rst_n == 1'b1) ? 1'b0 : i_rv_rst_n;
    // BUS rst_n
    assign bus_rst_n = i_rv_rst_n || i_spi_rst_n;


    core #(
        .RESET_PC               (RESET_PC)
    ) core_0 (
        .i_clk                  (i_clk),
        .i_rst_n                (i_rv_rst_n),

        // instruction interface
        .o_instr_addr           (instr_addr),
        .i_instr_rd_data        (instr_rd_data),
        .o_instr_wr_data        (instr_wr_data),
        .o_instr_size           (instr_size),
        .o_instr_read           (instr_read),
        .o_instr_write          (instr_write),

        // data interface
        .o_req_dmem             (req_data),
        .i_gnt_dmem             (gnt_data),
        .o_data_addr            (data_addr),
        .i_data_rd_data         (data_rd_data),
        .o_data_wr_data         (data_wr_data),
        .o_data_size            (data_size),
        .o_data_read            (data_read),
        .o_data_write           (data_write),

        // dma status
        .i_dma_busy             (dma_busy),

        // dma interface
        .o_dma_en               (dma_en),
        .o_dma_funct3           (dma_funct3),
        .o_dma_sel_pim          (dma_sel_pim),
        .o_dma_size             (dma_trans_size),
        .o_dma_mem_addr         (dma_mem_addr)
    );

    ids_dma #(
        .PIM_CTRL               (32'h4000_0010),
        .PIM_R                  (32'h4000_0020),
        .PIM_W_WEIGHT           (32'h4000_0040),
        .PIM_W_ACTIVATION       (32'h4000_0080)
    ) dma_0 (
        .i_clk                  (i_clk),
        .i_rst_n                (i_rv_rst_n),
        // CORE interface
        .i_dma_en               (dma_en),
        .i_funct3               (dma_funct3),
        .i_sel_pim              (dma_sel_pim),
        .i_size                 (dma_trans_size),      
        .i_mem_addr             (dma_mem_addr),
        // BUS interface
        .o_bus_req              (req_dma),
        .i_bus_gnt              (gnt_dma),
        .o_dma_addr             (dma_addr),
        .o_dma_write            (dma_write),
        .o_dma_read             (dma_read),
        .o_dma_size             (dma_size),
        .o_dma_wr_data          (dma_wr_data),
        .i_dma_rd_data          (dma_rd_data),
        // busy signal
        .o_dma_busy             (dma_busy)
    );


    // IDS BUS
    ids_bus bus_0 (
        .i_clk                  (i_clk), 
        .i_rst_n                (bus_rst_n),

    // MASTERS
    // RV IMEM
        .i_imem_addr            (instr_addr),
        .i_imem_write           (instr_write),
        .i_imem_read            (instr_read),
        .i_imem_size            (instr_size),
        .i_imem_din             (instr_wr_data),
        .o_imem_dout            (instr_rd_data),

    // SPI SLAVE
        .i_req_spi              (req_spi),
        .o_gnt_spi              (gnt_spi),
        .i_spi_addr             (spi_addr),
        .i_spi_write            (spi_write),
        .i_spi_read             (spi_read),
        .i_spi_size             (spi_size),
        .i_spi_din              (spi_wr_data),
        .o_spi_dout             (spi_rd_data),

    // RV DMEM
        .i_req_dmem             (req_data),
        .o_gnt_dmem             (gnt_data),
        .i_dmem_addr            (data_addr),
        .i_dmem_write           (data_write),
        .i_dmem_read            (data_read),
        .i_dmem_size            (data_size),
        .i_dmem_din             (data_wr_data),
        .o_dmem_dout            (data_rd_data),

    // DMA
        .i_req_dma              (req_dma),
        .o_gnt_dma              (gnt_dma),
        .i_dma_addr             (dma_addr),
        .i_dma_write            (dma_write),
        .i_dma_read             (dma_read),
        .i_dma_size             (dma_size),
        .i_dma_din              (dma_wr_data),
        .o_dma_dout             (dma_rd_data),

    // SLAVES
    // IMEM SRAM (IMEM port)
        .o_imem_addr            (imem_addr),
        .o_imem_write           (imem_write),
        .o_imem_read            (imem_read),
        .o_imem_size            (imem_size),
        .o_imem_din             (imem_wr_data),
        .i_imem_dout            (imem_rd_data),

    // DMEM SRAM (DMEM port)
        .o_dmem_addr            (dmem_addr),
        .o_dmem_write           (dmem_write),
        .o_dmem_read            (dmem_read),
        .o_dmem_size            (dmem_size),
        .o_dmem_din             (dmem_wr_data),
        .i_dmem_dout            (dmem_rd_data),

    // PIM BUFFER SRAM
        .o_buf_addr             (buf_addr),
        .o_buf_write            (buf_write),
        .o_buf_read             (buf_read),
        .o_buf_size             (buf_size),
        .o_buf_din              (buf_wr_data),
        .i_buf_dout             (buf_rd_data),  

    // UART
        .o_uart_addr            (uart_addr),
        .o_uart_write           (uart_write),
        .o_uart_read            (uart_read),
        .o_uart_size            (uart_size),
        .o_uart_din             (uart_wr_data),
        .i_uart_dout            (uart_rd_data),

    // PIM
        .o_pim_addr             (pim_addr),
        .o_pim_write            (pim_write),
        .o_pim_read             (pim_read),
        .o_pim_size             (pim_size),
        .o_pim_din              (pim_wr_data),
        .i_pim_dout             (pim_rd_data)
    );

    // SPI SLAVE
    spi_slave_wrap spi_slave_0 (
        .i_clk                  (i_clk),
        .i_rst_n                (i_spi_rst_n),
        // BUS I/F
        .o_req_spi              (req_spi),
        .i_gnt_spi              (gnt_spi),
        .o_spi_addr             (spi_addr),
        .i_spi_rd_data          (spi_rd_data),
        .o_spi_wr_data          (spi_wr_data),
        .o_spi_size             (spi_size),
        .o_spi_read             (spi_read),
        .o_spi_write            (spi_write),
        // SPI I/F
        .sclk                   (i_sclk),
        .cs                     (i_cs),
        .mosi                   (i_mosi),
        .miso                   (o_miso)
    );

    // IMEM
    sram_1024w_32b M0_0 (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (imem_read),
		.WEN			(~({4{imem_write}} & imem_size)),
		.A 				(imem_addr[11:2]),     // 10-bit address
		.D 				(imem_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(imem_rd_data)
	);

    // DMEM
    sram_1024w_32b M0_1 (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (dmem_read),
		.WEN			(~({4{dmem_write}} & dmem_size)),
		.A 				(dmem_addr[11:2]),
		.D 				(dmem_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(dmem_rd_data)
	);

    // weight and activation buffer
    sram_7168w_32b M1_0 (
		.CLK 			(i_clk),
		.CEN			(1'b0),
        .GWEN           (buf_read),
		.WEN			(~({4{buf_write}} & buf_size)),
		.A 				(buf_addr[14:2]),     // 10-bit address
		.D 				(buf_wr_data),
		.EMA			(3'b000),
		.RETN			(1'b1),
		// outputs
		.Q 				(buf_rd_data)
	);

    // on-chip uart
    uart_wrap #(
        .CLOCK_FREQ             (CPU_CLOCK_FREQ),
        .BAUD_RATE              (BAUD_RATE),
        .UART_CTRL              (32'h8000_0000),
        .UART_RECV              (32'h8000_0004),
        .UART_TRANS             (32'h8000_0008)
    ) on_chip_uart (
        .i_clk                  (i_clk), 
        .i_rst_n                (i_rv_rst_n), 
        .i_uart_addr            (uart_addr),
        .i_uart_write           (uart_write),
        .i_uart_read            (uart_read),
        .i_uart_size            (uart_size),
        .i_uart_din             (uart_wr_data),
        .o_uart_dout            (uart_rd_data),
        .i_serial_rx            (i_serial_rx),
        .o_serial_tx            (o_serial_tx)
    );

    assign o_pim_addr = pim_addr;
    assign o_pim_wr_data = pim_wr_data;
    assign pim_rd_data = i_pim_rd_data;

    // PIM WRAPPER
    //PIM_TOP pim_0 (
    //    .i_clk                  (i_clk),
    //    .i_rst                  (!rv_rst_n),
//
    //    // bus interface
    //    .i_address              (pim_addr),
    //    .i_data                 (pim_wr_data),
    //    .o_data                 (pim_rd_data),
//
    //    // pim interface
    //    .o_weight_out_en0       (),
    //    .o_weight_out_en1       (),
    //    .o_weight_out_en2       (),
    //    .o_weight_out_en3       (),
    //    .o_WL_address0          (),
    //    .o_WL_address1          (),
    //    .o_WL_address2          (),
    //    .o_WL_address3          (),
    //    .o_cam_data0            (),
    //    .o_cam_data1            (),
    //    .o_cam_data2            (),
    //    .o_cam_data3            (),
    //    .o_cim_data0            (),
    //    .o_cim_data1            (),
    //    .o_cim_data2            (),
    //    .o_cim_data3            (),
    //    .o_activation_out_en0   (),
    //    .o_activation_out_en1   (),
    //    .o_activation_out_en2   (),
    //    .o_activation_out_en3   (),
    //    .o_activation_out_data0 (),
    //    .o_activation_out_data1 (),
    //    .o_activation_out_data2 (),
    //    .o_activation_out_data3 (),
    //    .i_result_in0           (),
    //    .i_result_in1           (),
    //    .i_result_in2           (),
    //    .i_result_in3           ()
    //);


endmodule
