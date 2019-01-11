import time
from datetime import datetime
import threading
import winsound

dormir = 1
pin = 9


def hilo_fecha():
    global dormir
    global pin
    while True:
        ahora = datetime.today()
        print(dormir, ahora.second, pin)
        winsound.Beep(350, 500)
        time.sleep(dormir)


def hilo_entrada():
    global dormir
    global pin
    continuar = True
    while continuar:
        pin = int(input("Pin: "))
        dormir = int(input("Segundos: "))
        if pin == 0:
            continuar = False


if __name__ == '__main__':
    print("Iniciando")
    t = threading.Thread(target=hilo_fecha, daemon=True)
    t.start()
    z = threading.Thread(target=hilo_entrada, daemon=False)
    z.start()
    print("Finalizando")
