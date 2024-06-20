# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

TOPLEVEL_LANG ?= verilog
# CORE HEADERS
VERILOG_SOURCES += $(shell pwd)/../../rtl/headers/pipe_reg.svh
VERILOG_SOURCES += $(shell pwd)/../../rtl/headers/opcode.svh

# CORE
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core_top.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core_if_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core_id_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core_ex_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/core_wb_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/program_counter.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/main_control_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/immediate_generator.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/register_file.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/branch_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/forwarding_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/alu_control_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/alu.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/stall_generator.sv

# DMA
VERILOG_SOURCES += $(shell pwd)/../../rtl/dma/ids_dma.sv


# SPI SLAVE
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/spi_slave/spi_slave_wrap.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/spi_slave/spi_slave.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/spi_slave/RisingEdgeDetector.sv

# UART 
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart/uart_wrap.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart/uart.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart/uart_transmitter.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart/uart_receiver.v

# PIM WRAPPER 
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/activation_buffer2.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/dmux.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/pim_controller.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/result_buffer.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/weight_buffer.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/pim_wrap/PIM_TOP.v

# BUS
VERILOG_SOURCES += $(shell pwd)/../../rtl/bus/ids_bus.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/bus/ids_arbiter.sv

# MEMORY
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/imem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/dmem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/pim_buffer.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/sram_4k.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/sram_28k.v


TOPLEVEL = core_top
MODULE = test_asm

include $(shell cocotb-config --makefiles)/Makefile.sim