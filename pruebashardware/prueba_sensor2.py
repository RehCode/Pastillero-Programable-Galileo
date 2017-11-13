#!/usr/bin/python
'''
Activar el buzzer al transcurrir un tiempo de sensado
'''
import mraa
import time

buzzer = mraa.Gpio(7)
buzzer.dir(mraa.DIR_OUT)

led = mraa.Gpio(6)
led.dir(mraa.DIR_OUT)

sensor = mraa.Aio(0)

tiempo = False
inicio = time.time()
transcurrido = 0
limite_sec = 15
while True:
    sensado = sensor.read()

    if sensado <= 70: # ajustar
        led.write(1)
        # tomar tiempo
        if not tiempo:
            inicio = time.time()
            tiempo = True
        transcurrido = time.time() - inicio
        if transcurrido >= limite_sec:
            buzzer.write(1)
    else:
        led.write(0)
        buzzer.write(0)
        tiempo = False

    print(sensor.read())
    time.sleep(0.2)
