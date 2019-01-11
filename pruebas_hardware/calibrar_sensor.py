#!/usr/bin/python
'''
Guardar valor del sensor sin ninguna pastilla en superficie
'''
import mraa
import time

led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
sensor = mraa.Aio(0)
valor_con_pastilla = 0

# sin pastilla
print('2 Segundos para iniciar..')
time.sleep(2)
print('Sensado con pastilla')

for i in range(2):
    led.write(1)
    time.sleep(0.6)
    led.write(0)
    time.sleep(0.4)
    valor_con_pastilla = sensor.read()

print('Valor sensado:', valor_con_pastilla)

with open('valor_sensor.txt', 'w') as archivo:
    archivo.write(str(valor_con_pastilla))

# salida
time.sleep(1)
led.write(1)
time.sleep(1)
led.write(0)