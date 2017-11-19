#!/usr/bin/python
"""
 gira un servo del 0 a 180 en 30
"""
import mraa
import time

class Contenedor():
    MAXIMO = 0.14
    MINIMO = 0.04
    SEIS = [0, 30, 60, 90, 120, 150, 180]
    CUATRO = [0, 45, 90, 135, 180]
    TRES = [0, 60, 120, 180]
    def __init__(self, pin, nombre='uno', secciones=6):
        self.gpio = mraa.Pwm(pin)
        self.gpio.period_ms(20)
        self.gpio.enable(True)
        self.nombre = nombre
        self.seccion = 0

        self.numero_secciones = secciones
        if self.numero_secciones == 6:
            self.angulos = self.SEIS
        elif self.numero_secciones == 4:
            self.angulos = self.CUATRO
        else:
            self.numero_secciones = 3
            self.angulos = self.TRES

    def girar(self, angulo):
        if angulo <= 0:
            angulo = 0
        if angulo >= 180:
            angulo = 180

        duty = ((angulo / 18) + 4) / 100.0
        self.gpio.write(duty)
        self.angulo = angulo
        self.duty = duty

    def siguiente(self):
        self.seccion += 1
        if self.seccion > self.numero_secciones:
            self.seccion -= 1
            return False
        else:
            angulo = self.angulos[self.seccion]
            self.girar(angulo)
            return True

    def reset(self):
        self.seccion = 0
        self.girar(self.angulos[self.seccion])

cont1 = Contenedor(9, nombre='cont1', secciones=6)
resets = 0
while resets < 4:
    movio = cont1.siguiente()
    print(movio)
    if not movio:
        cont1.reset()
        resets += 1
        print(reset)
    time.sleep(2)