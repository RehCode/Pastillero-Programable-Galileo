#!/usr/bin/python
'''
Guardar valor del sensor sin ninguna pastilla en superficie
'''
import mraa
import time

led = mraa.Gpio(6)
led.dir(mraa.DIR_OUT)
sensor = mraa.Aio(0)
valor_con_pastilla = 0

# inicio
def blink(n=2):
    for i in range(n):
        led.write(1)
        time.sleep(0.6)
        led.write(0)
        time.sleep(0.4)

# sin pastilla
print('5 Segundos para iniciar..')
time.sleep(5)
blink(5)
print('Sensado sin pastilla')
valor_con_pastilla = sensor.read()
print('Valor sensado:', valor_con_pastilla)

with open('valor_sensor.txt', 'w') as archivo:
    archivo.write(str(valor_con_pastilla))
