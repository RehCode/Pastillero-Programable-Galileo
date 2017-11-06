#!/usr/bin/python
"""
    prueba encender buzzer con sensor o boton
"""

import mraa
import time
 
buzzer = mraa.Gpio(7)
buzzer.dir(mraa.DIR_OUT)

adc = mraa.Aio(0)

boton = mraa.Gpio(6)
boton.dir(mraa.DIR_IN)
boton.mode(mraa.MODE_PULLUP)

estado = 1
conteo = 0

while True:
    luz = adc.read()
    estado_boton = boton.read()
    if luz <= 70 or estado_boton == 0: # ajustar
        buzzer.write(1)
    else:
        buzzer.write(0)

    if estado_boton == 0:
        print("Boton presionado %d" % conteo)
        conteo += 1

    print(adc.read())
    time.sleep(0.2)

    if conteo >= 7:
        buzzer.write(0)
        break
