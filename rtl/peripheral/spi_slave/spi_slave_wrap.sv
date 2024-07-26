/*
    CS must released and reactivated between blocks (1 byte),
    Use "write_byte" function in spidev
*/

module spi_slave_wrap (
    // SYSTEM CLOCK
    input                   i_clk,
    input                   i_rst_n,
    // BUS INTERFACE
    output logic            o_req_spi,
    input                   i_gnt_spi,
    output logic    [31:0]  o_spi_addr,
    input           [31:0]  i_spi_rd_data,
    output logic    [31:0]  o_spi_wr_data,
    output logic    [ 3:0]  o_spi_size,
    output logic            o_spi_read,
    output logic            o_spi_write,
    // SPI SLAVE INTERFACE
    input                   sclk,
    input                   cs,
    input                   mosi,
    output logic            miso
);

    // Commands
    localparam ADDR_MODE    = 8'h1;
    localparam DATA_MODE    = 8'h2;

    // FSM states
    localparam IDLE         = 3'b000;
    localparam WAIT_CMD     = 3'b001;
    localparam READ_ADDR    = 3'b010;
    localparam READ_DATA    = 3'b011;
    localparam BUS_WRITE    = 3'b100;

    // state registers
    logic [2:0] curr_state;
    logic [2:0] next_state;

    // buffers
    logic [31:0] addr_buf;
    logic [31:0] data_buf;

    // Rising Edge Detection
    logic rising_cs;

    // data from spi slave
    logic [31:0] recv_data;
    logic [7:0] recv_cmd;

    // counter
    logic [2:0] recv_counter;
    logic count_start;
    logic recv_running;

    // read address and data
    logic write_addr;
    logic write_data;
    logic [31:0] read_addr;
    logic [31:0] read_data;

    // --|cmd parsing|-----------------------------------------------------------
    assign recv_cmd = recv_data[7:0];

    // --|register update|-----------------------------------------------------------
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            read_addr <= '0;
            read_data <= '0;
        end else begin
            if (write_addr) begin
                read_addr <= recv_data;
            end else begin
                read_addr <= read_addr;
            end
            if (write_data) begin
                read_data <= recv_data;
            end else begin
                read_data <= read_data;
            end
        end
    end

    // --|counter|-----------------------------------------------------------
    assign recv_running = recv_counter != '0;
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            recv_counter <= '0;
        end else begin
            if (count_start) begin
                recv_counter <= 4;
            end else if (rising_cs && recv_running) begin    // while running
                recv_counter <= recv_counter - 1;
            end
        end
    end    

    // --|FSM|------------------------------------------------------------
    // state transition
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (i_rst_n == '0) begin
            curr_state <= IDLE;
        end else begin
            curr_state <= next_state;
        end
    end

    // next state logic 
    always_comb begin
        case (curr_state)
            IDLE: begin
                next_state = WAIT_CMD;
            end 
            WAIT_CMD: begin
                if (rising_cs) begin
                    case (recv_cmd)
                        8'h1: begin
                            next_state = READ_ADDR;
                        end
                        8'h2: begin
                            next_state = READ_DATA;
                        end 
                        default: begin
                            next_state = WAIT_CMD;
                        end
                    endcase
                end else begin  
                    next_state = WAIT_CMD;
                end
            end 
            READ_ADDR: begin
                if (recv_running) begin
                    next_state = READ_ADDR;
                end else begin
                    next_state = WAIT_CMD;
                end
            end
            READ_DATA: begin
                if (recv_running) begin
                    next_state = READ_DATA;
                end else begin
                    next_state = BUS_WRITE;
                end
            end 
            BUS_WRITE: begin
                next_state = WAIT_CMD;
            end
            default: begin
                next_state = IDLE;
            end
        endcase
    end

    // output logic 
    always_comb begin
        count_start = '0;
        o_req_spi = '0;
        write_addr = '0;
        write_data = '0;
        // bus interface
        o_spi_addr = '0;
        o_spi_wr_data = '0;
        o_spi_size = '0;
        o_spi_read = '0;
        o_spi_write = '0;
        case (curr_state)
            WAIT_CMD: begin
                if (rising_cs) begin
                    if ((recv_cmd == 8'h1) || (recv_cmd == 8'h2)) begin
                        count_start = 1'b1;
                    end else begin
                        count_start = '0;
                    end
                end else begin 
                    count_start = '0;
                end
            end
            READ_ADDR: begin
                if (recv_running) begin
                    write_addr = 1'b1;
                end else begin
                    write_addr = 1'b0;
                end
            end
            READ_DATA: begin
                if (recv_running) begin
                    write_data = 1'b1;
                end else begin
                    o_req_spi = 1'b1;
                    write_data = 1'b0;
                end
            end 
            BUS_WRITE: begin
                // if grant write data
                if (i_gnt_spi) begin
                    o_spi_addr = read_addr;
                    o_spi_wr_data = read_data;
                    o_spi_size = 4'b1111;
                    o_spi_write = 1'b1;
                end else begin
                    o_spi_addr = '0;
                    o_spi_wr_data = '0;
                    o_spi_size = '0;
                    o_spi_write = '0;
                end
            end
            default: begin
                count_start = '0;
                o_req_spi = '0;
                write_addr = '0;
                write_data = '0;
                // bus interface
                o_spi_addr = '0;
                o_spi_wr_data = '0;
                o_spi_size = '0;
                o_spi_read = '0;
                o_spi_write = '0;
            end
        endcase
    end


    RisingEdgeDetector RED(
        .i_clk      (i_clk),
        .i_signal   (cs),
        .o_edge     (rising_cs)
    );
    
    spi_slave spi_slave(
        .i_clk      (i_clk),
        .i_rst_n    (i_rst_n),
        .i_sclk     (sclk),
        .i_ss_n     (cs),
        .i_mosi     (mosi),
        .o_miso     (miso),
        // we only receive data from external spi master
        .i_data     ('0),
        .o_data     (recv_data)
    );

endmodule