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
async def rvtest_add(dut):

    dut.RVRSTN.value = 0

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    for idx in range (0, 448):
        dut.M1_0.mem[idx].value = random.randint(0, 2**9)
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # program initialization
    imem_path = "../../software/asm_tests/add.hex"
    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"



@cocotb.test()
async def rvtest_sub(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sub.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

    

@cocotb.test()
async def rvtest_xor(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/xor.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_or(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/or.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_and(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/and.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sll(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sll.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_srl(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/srl.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_slt(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/slt.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sltu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sltu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_addi(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/addi.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_xori(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/xori.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_ori(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/ori.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_andi(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/andi.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_slli(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/slli.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_srli(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/srli.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_srai(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/srai.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_slti(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/slti.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sltiu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sltiu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lb(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lb.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lh(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lh.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lw(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lw.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lbu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lbu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lhu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lhu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sb(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sb.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sh(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sh.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_sw(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/sw.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_beq(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/beq.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_bne(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/bne.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_blt(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/blt.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_bge(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/bge.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_bltu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/bltu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_bgeu(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/bgeu.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_jal(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/jal.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_jalr(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/jalr.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_lui(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/lui.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"

@cocotb.test()
async def rvtest_auipc(dut):

    
    dut.RVRSTN.value = 0
    # memory initialization
    imem_path = "../../software/asm_tests/auipc.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.CLK, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.M0_0.mem[idx].value = 0
        dut.M0_1.mem[idx].value = 0
    await RisingEdge(dut.CLK)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.M0_0.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_0.mem[row_addr].value = data
            else:
                ddata =  dut.M0_1.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.M0_1.mem[row_addr].value = ddata
            await RisingEdge(dut.CLK)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.RVRSTN.value = 1

    for _ in range(1000):
        
        await RisingEdge(dut.CLK)

    assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"