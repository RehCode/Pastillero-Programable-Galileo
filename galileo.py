import mraa

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

        duty = ((angulo/18)+4)/100.0
        self.gpio.write(duty)


class Led():
    def __init__(self, pin, nombre):
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
        print("pin {} encendido".format(self.pin))
    
    def apagar(self):
        self.gpio.write(0)
        self.on = False
        print("pin {} apagado".format(self.pin))
