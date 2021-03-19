#Programa basico SPI 74H595
import machine
import utime

spi_sck = machine.Pin(2) #Clock
spi_tx = machine.Pin(3) #MOSI
spi_rx = machine.Pin(4) #MISO
cs = machine.Pin(5, machine.Pin.OUT) #Chip Select

cs.value(1)
#se inicializa el SPI
spi = machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx, miso=spi_rx, bits=8)

#Programa principal
cs.value(0)
index = 0b00001010
dato = bytes([int(index)])
spi.write(dato)
cs.value(1)

    