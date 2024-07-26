
module bus_arbiter (
    input           i_clk,
    input           i_rst_n,

    // master 1 (SPI)
    input           i_req_spi,
    output logic    o_gnt_spi,

    // master 2 (DMEM)
    input           i_req_dmem,
    output logic    o_gnt_dmem,

    // master 3 (DMA)
    input           i_req_dma,
    output logic    o_gnt_dma
);

    localparam IDLE     = 2'b00;
    localparam GNT_SPI  = 2'b01;
    localparam GNT_RV   = 2'b10;   // RV grant
    localparam GNT_DMA  = 2'b11;   // DMA grant

    logic [1:0] curr_state;
    logic [1:0] next_state;

    // state machine
    always_ff @ (posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
            curr_state <= IDLE;
        end else begin
            curr_state <= next_state;
        end
    end

    // next state machine
    always_comb begin
        case (curr_state)
            IDLE: begin
                if (i_req_spi) begin
                    next_state = GNT_SPI;
                end else if (i_req_dmem) begin
                    next_state = GNT_RV;
                end else if (i_req_dma) begin
                    next_state = GNT_DMA;
                end else begin
                    next_state = IDLE;
                end
            end
            GNT_SPI: begin
                if (i_req_spi) begin
                    next_state = GNT_SPI;
                end else begin
                    next_state = IDLE;
                end
            end
            GNT_RV: begin
                if (i_req_dmem) begin
                    next_state = GNT_RV;
                end else if (i_req_dma) begin
                    next_state = GNT_DMA;
                end else begin
                    next_state = IDLE;
                end
            end
            GNT_DMA: begin
                if (i_req_dmem) begin
                    next_state = GNT_RV;
                end else if (i_req_dma) begin
                    next_state = GNT_DMA;
                end else begin
                    next_state = IDLE;
                end
            end 
	    // DEFAULT branch of CASE statement cannot be reached
            //default: begin
            //    next_state = IDLE;
            //end
        endcase
    end

    // state output machine
    always_comb begin
        o_gnt_spi = '0;
        o_gnt_dmem = '0;
        o_gnt_dma = '0;
        case (curr_state)
            GNT_SPI: begin
                o_gnt_spi = 1'b1;
            end
            GNT_RV: begin                    // RV grant (DMEM)
                o_gnt_dmem = 1'b1;
            end
            GNT_DMA: begin                    // DMA grant
                o_gnt_dma = 1'b1;
            end 
            default: begin
                o_gnt_spi = '0;
                o_gnt_dmem = '0;
                o_gnt_dma = '0;
            end
        endcase
    end
    


endmodule
