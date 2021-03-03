#Programa que enciende el led externo con el boton
import machine
import utime

led_ext = machine.Pin(15, machine.Pin.OUT)
boton = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)


while True:
    if boton.value() == 1:
        led_ext.value(True)
        utime.sleep(2)
    led_ext.value(False)
    

    