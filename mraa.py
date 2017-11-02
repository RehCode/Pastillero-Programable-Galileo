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
        pass

    def mode(self, mode):
        pass


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
        pass
