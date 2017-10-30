import mraa
import time
import threading


servo_pin = 6
boton_pin = 8
sensor_pin = a0

class Servo():
    MAXIMO = 0.14
    MINIMO = 0.04
    def __init__(self, pin):
        self.gpio = mraa.Pwm(pin)
        self.gpio.period_ms(20)
        self.gpio.enable(True)
    
    def girar(self, angulo):
        if angulo <= 0:
            angulo = 0
        if angulo >= 180:
            angulo = 180
        
        duty = ((angulo/18)+4)/100
        self.gpio.write(duty)


class Led():
    def __init__(self, pin, duracion):
        self.gpio = mraa.Gpio(pin)
        self.gpio.dir(mraa.DIR_OUT)
        self.on = False
        self.dormir = duracion

    def encendido(self):
        return self.on
    
    def encender(self):
        self.gpio.write(1)
        self.on = True
    
    def apagar(self):
        self.gpio.write(0)
        self.on = False

# configuracion leds
verde = Led(13, 3)
rojo = Led(12, 4)
amarillo = Led(11, 1)

def hilo_led(led):
    while True:
        if led.encendido():
            led.apagar()
        else:
            led.ecender()
        time.sleep(led.duracion)

if __name__ == '__main__':
    tv = threading.Thread(target=hilo_led, args=(verde, ), daemon=True)
    tv.start()
    tv = threading.Thread(target=hilo_led, args=(rojo, ), daemon=True)
    tv.start()
    tv = threading.Thread(target=hilo_led, args=(amarillo, ), daemon=True)
    tv.start()