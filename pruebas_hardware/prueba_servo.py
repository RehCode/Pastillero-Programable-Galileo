#!/usr/bin/python
"""
 gira un servo del 0 a 180 en 30
"""
import mraa
import time


class Servo():
    MAXIMO = 0.14
    MINIMO = 0.04

    def __init__(self, pin, nombre='uno'):
        self.gpio = mraa.Pwm(pin)
        self.gpio.period_ms(20)
        self.gpio.enable(True)
        self.nombre = nombre

    def girar(self, angulo):
        if angulo <= 0:
            angulo = 0
        if angulo >= 180:
            angulo = 180

        duty = ((angulo / 18) + 4) / 100.0
        self.gpio.write(duty)


servo = Servo(9)

for angulo in range(0, 190, 30):
    servo.girar(angulo)
    time.sleep(3)
