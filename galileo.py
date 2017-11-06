import mraa

class Servo():
    MAXIMO = 0.14
    MINIMO = 0.04
    def __init__(self, pin, nombre='servo1'):
        self.gpio = mraa.Pwm(pin)
        self.gpio.period_ms(20)
        self.gpio.enable(True)
        self.nombre = nombre
    
    def girar(self, angulo):
        if angulo <= 0:
            angulo = 0
        if angulo >= 180:
            angulo = 180

        duty = ((angulo/18)+4)/100.0
        self.gpio.write(duty)


class Led():
    def __init__(self, pin, nombre='led'):
        self.gpio = mraa.Gpio(pin)
        self.gpio.dir(mraa.DIR_OUT)
        self.on = False
        self.nombre = nombre
        self.pin = pin

    def encendido(self):
        return self.on
    
    def encender(self):
        self.gpio.write(1)
        self.on = True
    
    def apagar(self):
        self.gpio.write(0)
        self.on = False


class Adc(object):
    def __init__(self, pin, nombre='sensor1'):
        self.aio = mraa.Aio(pin)
        self.pin = pin
        self.nombre = nombre

    def leer(self):
        return self.aio.read()


class Boton(object):
    """Clase para crear un boton con pin pullup"""
    def __init__(self, pin, nombre='boton1'):
        self.gpio = mraa.Gpio(pin)
        self.gpio.dir(mraa.DIR_IN)
        self.gpio.mode(mraa.MODE_PULLUP)
        self.nombre = nombre
        self.pin = pin
    
    def leer_estado(self):
        return self.gpio.read()
