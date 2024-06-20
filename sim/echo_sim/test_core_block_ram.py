# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# test_my_design.py (simple)

import os
import random
from pathlib import Path
import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge
from cocotb.triggers import Timer
from cocotb.types import LogicArray


@cocotb.test()
async def core_bench(dut):

    dut.i_rst_n.value = 0
    
    for idx in range (0, 1024):
        dut.top.imem_0.imem_sram.d0[idx].value = 0
        dut.top.imem_0.imem_sram.d1[idx].value = 0
        dut.top.imem_0.imem_sram.d2[idx].value = 0
        dut.top.imem_0.imem_sram.d3[idx].value = 0
        dut.top.dmem_0.dmem_sram.d0[idx].value = 0
        dut.top.dmem_0.dmem_sram.d1[idx].value = 0
        dut.top.dmem_0.dmem_sram.d2[idx].value = 0
        dut.top.dmem_0.dmem_sram.d3[idx].value = 0
    # program initialization
    imem_path = "../../software/echo_bios/echo_bios.hex"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            if idx < 1024:
                dut.top.imem_0.imem_sram.d0[idx].value = (inst_decimal & 0x000000ff)
                dut.top.imem_0.imem_sram.d1[idx].value = (inst_decimal & 0x0000ff00) >> 8
                dut.top.imem_0.imem_sram.d2[idx].value = (inst_decimal & 0x00ff0000) >> 16
                dut.top.imem_0.imem_sram.d3[idx].value = (inst_decimal & 0xff000000) >> 24
            else:
                dut.top.dmem_0.dmem_sram.d0[idx-1024].value = (inst_decimal & 0x000000ff)
                dut.top.dmem_0.dmem_sram.d1[idx-1024].value = (inst_decimal & 0x0000ff00) >> 8
                dut.top.dmem_0.dmem_sram.d2[idx-1024].value = (inst_decimal & 0x00ff0000) >> 16
                dut.top.dmem_0.dmem_sram.d3[idx-1024].value = (inst_decimal & 0xff000000) >> 24
            idx = idx + 1

    # Create a 10ns period clock on port clk
    clock = Clock(dut.i_clk, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")
    

    await RisingEdge(dut.i_clk)
    dut.i_rst_n.value = 1

    for _ in range(5):
        await RisingEdge(dut.i_clk)
        await Timer(1, units="ns")

    done = 0

    while True:
        if dut.data_in_ready.value == 1:
            print("SEND: ", end="")
            data = input()
            dut.data_in.value = ord(data)
            dut.data_in_valid.value = 1
            await RisingEdge(dut.i_clk)
            await Timer(1, units="ns")
            dut.data_in.value = 0
            dut.data_in_valid.value = 0
            break
            
        else:
            await RisingEdge(dut.i_clk)
            await Timer(1, units="ns")

    while True:
        if dut.data_out_valid.value == 1:
            print("Got ", chr(int(dut.data_out.value.binstr,2)))
            break
            
        else:
            await RisingEdge(dut.i_clk)
            await Timer(1, units="ns")

    for _ in range (5):
        await RisingEdge(dut.i_clk)
        await Timer(1, units="ns")



    #done = 0
    #send_done = 1
    #recv_done = 0
#
    #for clk in range(100000):
    #    while recv_done == 0:
    #        if dut.data_out_valid.value == 1:
    #            # last char
    #            if int(dut.data_out.value.binstr, 2) == 0x0d:
    #                print("", end="")
    #            elif int(dut.data_out.value.binstr, 2) == 0x00:
    #                recv_done = 1
    #                send_done = 0
    #            else:
    #                print(chr(int(dut.data_out.value.binstr, 2)), end="")
    #            dut.data_out_ready.value = 1
    #            await RisingEdge(dut.i_clk)
    #            await Timer(1, units="ns")
    #            dut.data_out_ready.value = 0
    #        else:
    #            await RisingEdge(dut.i_clk)
#
    #    read = input()
    #    read = read + '\r'
    #    i = 0
    #    while send_done == 0:
    #        if dut.data_in_ready.value == 1:
    #            dut.data_in.value = ord(read[i])
    #            if read[i] == '\r':
    #                recv_done = 0
    #                send_done = 1
    #            dut.data_in_valid.value = 1
    #            await RisingEdge(dut.i_clk)
    #            await Timer(1, units="ns")
    #            dut.data_in_valid.value = 0
    #            i = i + 1
    #        else:
    #            await RisingEdge(dut.i_clk)
#
    #    if done == 1:
    #        for _ in range(10):
    #            await RisingEdge(dut.i_clk)
    #        break
#
    #    await RisingEdge(dut.i_clk)