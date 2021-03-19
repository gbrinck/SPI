#Programa SPI potencias de 2 divertimento
import machine
import utime

spi_sck = machine.Pin(2) #Clock
spi_tx = machine.Pin(3) #MOSI
spi_rx = machine.Pin(4) #MISO
cs = machine.Pin(5, machine.Pin.OUT) #Chip Select

cs.value(1)
#Inicializa SPI
spi = machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx, miso=spi_rx, bits=8)
#Programa principal
while True:
    for index in range(4):
        index2 = 2**index
        cs.value(0)
        vari = bytes([int(index2)])
        spi.write(vari)
        cs.value(1)
        utime.sleep(.1)
    for index in range(2,0,-1):
        index2 = 2**index
        cs.value(0)
        vari = bytes([int(index2)])
        spi.write(vari)
        cs.value(1)
        utime.sleep(.1)


