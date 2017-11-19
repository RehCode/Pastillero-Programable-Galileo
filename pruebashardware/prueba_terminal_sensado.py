#!/usr/bin/python
'''
Activar el buzzer al transcurrir un tiempo de sensado
'''
import time

sensor = 50

dispensado = False
tiempo = False
inicio = time.time()
transcurrido = 0
limite_sec_pastilla = 2
limite_sec_buzzer = 7
tomadas = 0
with open('valor_sensor.txt') as archivo:
    valor_con_pastilla = int(archivo.readline())

print('valor_con_pastilla: ', valor_con_pastilla)
while True:
    sensado = int(input("Sensado: "))

    if sensado <= valor_con_pastilla: # ajustar
        print('Led On')
        # tomar tiempo
        if not tiempo:
            inicio = time.time()
            tiempo = True
        else:
            transcurrido = time.time() - inicio
            print('Tiempo: ', transcurrido)

            if transcurrido >= limite_sec_pastilla:
                dispensado = True

            if transcurrido >= limite_sec_buzzer:
                print('Buzzer On')
    else:
        print('Led Off')
        print('Buzzer Off')
        tiempo = False
        if dispensado:
            tomadas += 1
        dispensado = False

    if dispensado:
        print('Dispensado')
    print('tomadas: ', tomadas)
    print('---'*25)
    # time.sleep(0.2)
