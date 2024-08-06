
module rising_edge_detect (
    input           i_clk,
    input           i_signal,
    output  logic   o_edge
);

    logic prev_signal;

    always_ff @(posedge i_clk) begin
        prev_signal <= i_signal;
        o_edge <= (i_signal && !prev_signal);
    end


endmodule