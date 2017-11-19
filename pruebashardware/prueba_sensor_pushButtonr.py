#!/usr/bin/python
"""
    prueba de seguidor de lineas y boton
"""
import mraa
import time

adc = mraa.Aio(0)
boton = mraa.Gpio(6)
boton.dir(mraa.DIR_IN)
boton.mode(mraa.MODE_PULLUP)

estado = 1
conteo = 0

while True:
    estado = boton.read()
    if estado == 0:
        print("Boton presionado %d" % conteo)
        conteo += 1
    print(adc.read())
    time.sleep(0.3)

    if conteo >= 7:
        break
