'''
Mock de mraa
'''
DIR_OUT = 0
DIR_IN = 0
MODE_PULLUP = 1
MODE_PULLDOWN = 2
DIR_OUT = 0
DIR_IN = 1
DIR_OUT_HIGH = 2
DIR_OUT_LOW = 3

class Gpio(object):
    def __init__(self, pin):
        self.pin = pin

    def dir(self, dir):
        pass

    def write(self, value):
        if value == 1:
            print('{} ON'.format(self.pin))
        
        if value == 0:
            print('{} OFF'.format(self.pin))

    def mode(self, mode):
        pass
    
    def read(self):
        return 1


class Pwm(object):
    def __init__(self, pin):
        self.pin = pin

    def enable(self, enable):
        pass

    def period(self, period):
        pass

    def period_ms(self, ms):
        pass

    def write(self, percentaje):
        pass


class Aio(object):
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        with open('valor_sensor.txt') as archivo:
            valor = int(archivo.readline())
            return valor
