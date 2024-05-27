
module stall_generator (
    input                   i_clk,
    input                   i_rst_n,
    input                   i_stall_gen,
    input           [12:0]  i_stall_count,
    output  logic           o_stall
);
    logic [13:0] counter;
    logic count_running;
    logic count_start;
    logic [12:0] count_size;

    // --|counter|-----------------------------------------------------------
    assign count_running = counter != '0;
    assign count_start = i_stall_gen;
    assign count_size = i_stall_count;
    
    always_ff @(posedge i_clk or negedge i_rst_n) begin
        if (~i_rst_n) begin
            counter <= '0;
        end else begin
            if (count_start) begin
                counter <= ((count_size + 1) << 1); // extra one cycle for status read
            end else if (count_running) begin    // while running
                counter <= counter - 1;
            end
        end
    end  
    assign o_stall = (count_running) ? 1'b1: 1'b0;



endmodule