import threading, time, logging
from datetime import datetime
from bottle import route, run, template, request, redirect, static_file
from galileo import Led, Servo

logging.basicConfig(level=logging.DEBUG)
logging.debug("A debug message!")

datos_leds = {"rojo_seg": 13, "verde_seg": 17, "amarillo_min":22, "amarillo_hora":14, "dia": "lunes", "cambio":False}

servo = Servo(9)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

@route('/')
def raiz():
    return template('views/home.tpl', fecha=datetime.now().ctime())

@route('/angulos')
def angulos():
    return template('views/angulos.tpl', angulo=0)

@route('/angulos', method='POST')
def angulos_post():
    angulo = int(request.forms.get('angulo'))
    logging.debug(angulo)
    servo.girar(angulo)
    return template('views/angulos.tpl', angulo=angulo)

@route('/leds')
def leds():
    return template('views/leds.tpl', **datos_leds)


@route('/leds', method='POST')
def leds_post():
    global datos_leds

    rojoSeg = int(request.forms.get('rojoSeg'))
    verdeSeg = int(request.forms.get('verdeSeg'))
    amarilloHora = int(request.forms.get('amarilloHora'))
    amarilloMin = int(request.forms.get('amarilloMin'))
    dia = request.forms.get('dia')

    if datos_leds['amarillo_hora'] != amarilloHora:
        datos_leds['cambio'] = True
    elif datos_leds['amarillo_min'] != amarilloMin:
        datos_leds['cambio'] = True
    elif datos_leds['dia'] != dia:
        datos_leds['cambio'] = True
    else:
        datos_leds['cambio'] = False

    datos_leds['rojo_seg'] = rojoSeg
    datos_leds['verde_seg'] = verdeSeg
    datos_leds['amarillo_min'] = amarilloMin
    datos_leds['amarillo_hora'] = amarilloHora
    datos_leds['dia'] = dia

    redirect('/leds')

@route('/sensor')
def sensor():
    return template('views/sensor.tpl')

@route('/fecha')
def fecha():
    return datetime.now().ctime()


@route('/login')
def forma():
    return template('views/login.tpl', ok_login=True)


def check_login(username, password):
    if username == 'rene' and password == '123':
        return True
    else:
        return False


@route('/login', method='POST')
def do_login():
    usuario = request.forms.get('usuario')
    password = request.forms.get('password')
    if check_login(usuario, password):
        return template('views/programacion.tpl')
    else:
        return template('views/login.tpl', ok_login=False)


verde = Led(13, 'verde')
rojo = Led(12, 'rojo')
amarillo = Led(11, 'amarillo')

def hilo_led(led):
    global datos_leds
    llave_seg = led.nombre + '_seg'
    while True:
        if led.encendido():
            led.apagar()
        else:
            led.encender()

        tiempo = datos_leds[llave_seg]
        # print("esperando segundos de color {} -> {}".format(led.nombre, tiempo))
        time.sleep(tiempo)

def hilo_fecha(amarillo):
    global datos_leds
    nom_dia = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    dispensado = False                 
    while True:
        ahora = datetime.now()
        dia = ahora.weekday()

        if datos_leds['cambio']:
            dispensado = False
            datos_leds['cambio'] = False

        if nom_dia[ahora.weekday()] == datos_leds["dia"]:
            if ahora.hour == datos_leds["amarillo_hora"]:
                if ahora.minute == datos_leds["amarillo_min"] and not dispensado:
                    print("Dispensando medicina...")
                    amarillo.encender()
                    time.sleep(4)
                    amarillo.apagar()
                    dispensado = True
        
        time.sleep(5)
        # logging.debug(datos_leds)


if __name__ == '__main__':
    # python 2.7
    # t = threading.Thread(name='hilo_fecha', target=hilo)
    # t.setDaemon(True)
    # t.start()

    tv = threading.Thread(target=hilo_led, args=(verde, ), daemon=True)
    tv.start()
    tr = threading.Thread(target=hilo_led, args=(rojo, ), daemon=True)
    tr.start()
    tr = threading.Thread(target=hilo_fecha, args=(amarillo, ), daemon=True)
    tr.start()    
    run(host='0.0.0.0', port=8080, debug=True)