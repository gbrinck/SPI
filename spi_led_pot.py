#Programa SPI controlado por potenciometro
import machine
import utime

spi_sck = machine.Pin(2) #Clock
spi_tx = machine.Pin(3) #MOSI
spi_rx = machine.Pin(4) #MISO
cs = machine.Pin(5, machine.Pin.OUT) #Chip Select
#Potenciometro en GPIO27
pot = machine.ADC(27)

cs.value(1)
#Inicializa SPI
spi = machine.SPI(0,baudrate=100000,sck=spi_sck, mosi=spi_tx, miso=spi_rx, bits=8)
#Programa principal
while True:
    for index in range(16):
        cs.value(0)
        dato = bytes([int(index)])
        spi.write(dato)
        cs.value(1)
        espera = int((pot.read_u16()/65535)*1000) 
        utime.sleep_ms(espera)