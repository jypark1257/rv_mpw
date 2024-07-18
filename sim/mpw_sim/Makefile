#HEADERS
HEADERS := $(wildcard ./../../rtl/headers/*.svh)

# CORE
CORESRCS := $(wildcard ./../../rtl/core/*.sv)

# DMA
DMASRCS := $(wildcard .//../../rtl/dma/*.sv)

# SPI SLAVE
SPISRCS := $(wildcard ./../../rtl/peripheral/spi_slave/*.sv)

# UART 
UARTVSRCS := $(wildcard .//../../rtl/peripheral/uart/*.v)
UARTSVSRCS := $(wildcard .//../../rtl/peripheral/uart/*.sv)

# BUS
BUSSRCS := $(wildcard ./../../rtl/bus/*.sv)

# MEMORY
MEMSRCS := $(wildcard ./../../rtl/memory/*.v)
 
all: 
	iverilog -g2012 ./mpw_sim.sv ./spi_master.sv $(HEADERS) $(CORESRCS) $(DMASRCS) $(SPISRCS) $(UARTVSRCS) $(UARTSVSRCS) $(BUSSRCS) $(MEMSRCS)
dump:
	vvp ./a.out
show: 
	gtkwave ./dump.vcd &