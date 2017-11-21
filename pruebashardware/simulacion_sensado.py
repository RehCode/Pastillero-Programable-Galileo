#!/usr/bin/python
'''
Encender led cuando se obstruye el sensor con una pastilla
Activar el buzzer al transcurrir un tiempo de sensado
Contar las veces que se retira la pastilla del sensor
'''
import mraa
import time

buzzer = mraa.Gpio(12)
buzzer.dir(mraa.DIR_OUT)

led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)

sensor = mraa.Aio(0)

dispensado = False
tiempo = False
inicio = time.time()
transcurrido = 0
limite_sec_pastilla = 2
limite_sec_buzzer = 15
tomadas = 0

with open('valor_sensor.txt') as archivo:
    valor_con_pastilla = int(archivo.readline())

print('valor_con_pastilla: ', valor_con_pastilla)

while True:
    sensado = sensor.read()
    
    if sensado <= valor_con_pastilla: # ajustar
        
        # tomar tiempo
        if not tiempo:
            inicio = time.time()
            tiempo = True
        else:
            transcurrido = time.time() - inicio
            print('Tiempo trasncurrido: ', transcurrido)
            if transcurrido >= limite_sec_pastilla:
                dispensado = True
                
            if transcurrido >= limite_sec_buzzer:
                buzzer.write(1)
    else:
        led.write(0)
        buzzer.write(0)
        tiempo = False
        if dispensado:
            tomadas += 1        
        dispensado = False

    if dispensado:
        led.write(1)
        print('Dispensado')

    print(sensor.read())
    print('tomadas: ', tomadas)
    time.sleep(0.2)
