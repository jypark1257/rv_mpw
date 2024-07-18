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
import asyncio
from cocotbext.spi import *

async def write_sram(dut, spi_master, address, data):
    addr_0 = (address & 0xFF)
    addr_1 = (address & 0xFF00) >> 8
    addr_2 = (address & 0xFF0000) >> 16
    addr_3 = (address & 0xFF000000) >> 24
    data_0 = (data & 0xFF)
    data_1 = (data & 0xFF00) >> 8
    data_2 = (data & 0xFF0000) >> 16
    data_3 = (data & 0xFF000000) >> 24

    # address
    await spi_master.write([0x01])  # command
    await Timer(30, units="ns")
    await spi_master.write([addr_3])
    await Timer(30, units="ns")
    await spi_master.write([addr_2])
    await Timer(30, units="ns")
    await spi_master.write([addr_1])
    await Timer(30, units="ns")
    await spi_master.write([addr_0])
    await Timer(30, units="ns")
    # data
    await spi_master.write([0x02])  # command
    await Timer(30, units="ns")
    await spi_master.write([data_3])
    await Timer(30, units="ns")
    await spi_master.write([data_2])
    await Timer(30, units="ns")
    await spi_master.write([data_1])
    await Timer(30, units="ns")
    await spi_master.write([data_0])
    await Timer(30, units="ns")


@cocotb.test()
async def core_bench(dut):

    imem_path = "../../software/pim_instr_test/pim_instr.hex"

    dut.i_rv_rst_n.value = 0
    dut.i_spi_rst_n.value = 0

    # Create a 10ns period clock on port clk
    clock = Clock(dut.i_clk, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    # spi master
    spi_bus = SpiBus.from_entity(dut)
    spi_config = SpiConfig(
        word_width      = 8,
        sclk_freq       = 25e6,
        cpol            = False,
        cpha            = False,
        msb_first       = True,
        cs_active_low   = True
    )
    spi_master = SpiMaster(spi_bus, spi_config)

    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")
    dut.i_spi_rst_n.value = 1
    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")



# dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0x40000000
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            #print("addr: \t", hex(idx)[2:].zfill(8))
            #print("data: \t", hex(inst_decimal)[2:].zfill(8))
            
            await cocotb.start_soon(write_sram(dut, spi_master, idx, inst_decimal))
            idx = idx + 4
            #if idx == 0x4000007c:
            #    break


    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")
    dut.i_rv_rst_n.value = 1
    dut.i_spi_rst_n.value = 0
    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")

    for _ in range(10000):
        await RisingEdge(dut.i_clk)

    #assert dut.core_0.core_ID.rf.rf_data[3].value == 0xffffffff, "RVTEST_FAIL"






