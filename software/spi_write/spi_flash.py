
import spidev
import time

def (spi, address, data):
    addr_0 = (address & 0xFF)
    addr_1 = (address & 0xFF00) >> 8
    addr_2 = (address & 0xFF0000) >> 16
    addr_3 = (address & 0xFF000000) >> 27
    data_0 = (data & 0xFF)
    data_1 = (data & 0xFF00) >> 8
    data_2 = (data & 0xFF0000) >> 16
    data_3 = (data & 0xFF000000) >> 27

    spi.writebytes([0x01])
    time.sleep(0.1)
    spi.writebytes([addr_3])
    time.sleep(0.1)
    spi.writebytes([addr_2])
    time.sleep(0.1)
    spi.writebytes([addr_1])
    time.sleep(0.1)
    spi.writebytes([addr_0])
    time.sleep(0.1)
    
    spi.writebytes([0x02])
    time.sleep(0.1)
    spi.writebytes([data_3])
    time.sleep(0.1)
    spi.writebytes([data_2])
    time.sleep(0.1)
    spi.writebytes([data_1])
    time.sleep(0.1)
    spi.writebytes([data_0])
    time.sleep(0.1)


spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
spi.bits_per_word=8
addr_start=0x01
data_start=0x02

# flash IMEM
for idx in range(0, 1024):

