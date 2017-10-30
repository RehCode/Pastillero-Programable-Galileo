import time
from datetime import datetime
import threading
import winsound
import queue

dormir = queue.Queue()
dormir.put(1)

pin = queue.Queue()
pin.put(8)

def hilo_fecha():
    dormir_sec = 2
    pin_actual = 7

    while True:
        while not pin.empty():
            pin_actual = pin.get()

        while not dormir.empty():
            dormir_sec = dormir.get()

        ahora = datetime.today()
        print(dormir, ahora.second, pin_actual)
        winsound.Beep(350, 500)
        time.sleep(dormir_sec)


def hilo_entrada():
    continuar = True
    while continuar:
        pin_in = int(input("Pin: "))
        dormir_in = int(input("Segundos: "))
        if pin_in == 0:
            continuar = False
        else:
            pin.put(pin_in)
            dormir.put(dormir_in)


if __name__ == '__main__':
    print("Iniciando")
    t = threading.Thread(target=hilo_fecha, daemon=True)
    t.start()
    z = threading.Thread(target=hilo_entrada, daemon=False)
    z.start()
    print("Finalizando")
