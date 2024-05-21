# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

TOPLEVEL_LANG ?= verilog
# CORE
VERILOG_SOURCES += $(shell pwd)/../../rtl/core_top.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core_if_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core_id_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core_ex_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/core_wb_stage.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/program_counter.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/main_control_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/immediate_generator.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/register_file.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/branch_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/forwarding_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/alu_control_unit.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/alu.sv

# UART 
VERILOG_SOURCES += $(shell pwd)/../../rtl/uart.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/uart_transmitter.v
VERILOG_SOURCES += $(shell pwd)/../../rtl/uart_receiver.v

# BUS
VERILOG_SOURCES += $(shell pwd)/../../../ids_bus/rtl/ids_bus.sv
VERILOG_SOURCES += $(shell pwd)/../../../ids_bus/rtl/ids_arbiter.sv

# MEM
VERILOG_SOURCES += $(shell pwd)/../../rtl/imem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/dmem.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/sram_1k.sv
VERILOG_SOURCES += $(shell pwd)/../../rtl/sram_8_1024.v

TOPLEVEL = core_top
MODULE = test_core

include $(shell cocotb-config --makefiles)/Makefile.sim