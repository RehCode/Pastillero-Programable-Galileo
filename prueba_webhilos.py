import threading, time
from datetime import datetime
from bottle import route, run, template, request, redirect, static_file
from galileo import Led, Servo, Adc

datos_leds = {"amarillo_min":22, "amarillo_hora":14, "dia": "lunes", "cambio":False}
sensor_limite = 70
servo = Servo(9)

buzzer = Led(7, 'buzzer')
sensorh1 = Adc(0)

amarillo = Led(11, 'amarillo')

cont1_nombre = 'Aaspirina'
cont1_secciones = {
            'secc1': {'dia': 'lunes', 'hora': 14, 'minuto': 1},
            'secc2': {'dia': 'lunes', 'hora': 15, 'minuto': 2},
            'secc3': {'dia': 'lunes', 'hora': 16, 'minuto': 3},
            'secc4': {'dia': 'lunes', 'hora': 17, 'minuto': 4},
            'secc5': {'dia': 'lunes', 'hora': 18, 'minuto': 5},
            'secc6': {'dia': 'lunes', 'hora': 19, 'minuto': 6},
            }


def hilo_sensor(sensorh, buzzer):
    while True:
        luz = sensorh.leer()
        if luz <= sensor_limite: # ajustar
            buzzer.encender()
        else:
            buzzer.apagar()

        print('Sensor:', sensorh.leer())
        time.sleep(2)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

@route('/')
@route('/home')
def raiz():
    return template('views/home.tpl', fecha=datetime.now().ctime())

# --- comentarios
@route('/comentarios_vista')
def ver_comentarios():
    return template('comentarios_vista.tpl')

@route('/comentarios_ingreso')
def ingresar_comentarios():
    return template('comentarios_ingreso.tpl')

@route('/com_cont', method='POST')
def ingresar_comentarios():
    return template('comentarios_ingreso.tpl')

@route('/com_trat', method='POST')
def ingresar_comentarios():
    return template('comentarios_ingreso.tpl')

# --- estadisticas
@route('/estadisticas')
def estadistica():
    return template('estadisticas.tpl')

# --- contenedor 1
@route('/cont1')
def cont1():
    return template('cont1.tpl', cont1_secciones=cont1_secciones, cont1_nombre=cont1_nombre)

@route('/cont1', method='POST')
def cont1_prog():

    for seccion in list(cont1_secciones.keys()):
        for parametro in ['dia', 'hora', 'minuto']:
            if parametro == 'dia':
                cont1_secciones[seccion][parametro] = request.forms.get(seccion + 'Dia')
            if parametro == 'hora':
                cont1_secciones[seccion][parametro] = request.forms.get(seccion + 'Hora')
            if parametro == 'minuto':
                cont1_secciones[seccion][parametro] = request.forms.get(seccion + 'Min')
    cont1_nombre = request.forms.get('nombre')
    return template('cont1.tpl', cont1_secciones=cont1_secciones, cont1_nombre=cont1_nombre)


# --- sensor 1
@route('/sensor1')
def sensor():
    return template('views/sensor1.tpl', sensor_limite=sensor_limite)

@route('/sensor1', method='POST')
def sensor_set():
    global sensor_limite
    sensorLimite = int(request.forms.get('limiteLuz'))
    if sensorLimite != sensor_limite:
        sensor_limite = sensorLimite
    return template('views/sensor1.tpl', sensor_limite=sensor_limite)


@route('/fecha')
def fecha():
    return datetime.now().ctime()

# --- login
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


# test de sensores y mockup
@route('/angulos')
def angulos():
    return template('views/angulos.tpl', angulo=0)

@route('/angulos', method='POST')
def angulos_post():
    angulo = int(request.forms.get('angulo'))
    servo.girar(angulo)
    return template('views/angulos.tpl', angulo=angulo)

@route('/leds')
def leds():
    return template('views/leds.tpl', **datos_leds)


@route('/leds', method='POST')
def leds_post():
    global datos_leds

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

    datos_leds['amarillo_min'] = amarilloMin
    datos_leds['amarillo_hora'] = amarilloHora
    datos_leds['dia'] = dia

    redirect('/leds')


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
    import sys
    if sys.version_info[0] > 2:
        ta = threading.Thread(target=hilo_fecha, args=(amarillo, ), daemon=True)
        ta.start()
        tsensor = threading.Thread(target=hilo_sensor, args=(sensorh1, buzzer), daemon=True)
        tsensor.start()
    else:
        ta = threading.Thread(target=hilo_fecha, args=(amarillo, ))
        ta.setDaemon(True)
        ta.start()
        tsensor = threading.Thread(target=hilo_sensor, args=(sensorh1, buzzer))
        tsensor.setDaemon(True)
        tsensor.start()
    # python 2.7
    # t = threading.Thread(name='hilo_fecha', target=hilo)
    # t.setDaemon(True)
    # t.start()

    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
