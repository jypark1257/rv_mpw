module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/mpw_top.fst");
    $dumpvars(0, mpw_top);
end
endmodule
