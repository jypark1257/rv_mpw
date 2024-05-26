# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

TOPLEVEL_LANG ?= verilog
# CORE HEADERS
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/pipe_reg.svh
VERILOG_SOURCES += $(shell pwd)/../../rtl/core/opcode.svh

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

# UART 
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart_wrap.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart_transmitter.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/peripheral/uart_receiver.v

# BUS
VERILOG_SOURCES += $(shell pwd)/../../rtl/bus/ids_bus.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/bus/ids_arbiter.sv

# MEMORY
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/imem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/dmem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/memory/sram_4k.v

TOPLEVEL = core_top
MODULE = test_asm

include $(shell cocotb-config --makefiles)/Makefile.sim