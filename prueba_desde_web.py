import threading
from datetime import datetime
from bottle import route, run, template, request, redirect, static_file

datos_leds = {"seg_rojo": 5, "seg_verde": 7, "min_amarillo":22, "hora_amarillo":14, "dia": "lunes"}

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

@route('/')
def raiz():
    return template('views/home.tpl')

@route('/angulos')
def angulos():
    return template('views/angulos.tpl')

@route('/angulos', method='POST')
def angulos_post():
    redirect('/angulos')

@route('/leds')
def leds():
    return template('views/leds.tpl', **datos_leds)


@route('/leds', method='POST')
def leds_post():
    global datos_leds

    rojoSeg = request.forms.get('rojoSeg')
    verdeSeg = request.forms.get('verdeSeg')
    amarilloHora = request.forms.get('amarilloHora')
    amarilloMin = request.forms.get('amarilloMin')
    dia = request.forms.get('dia')

    datos_leds = {"seg_rojo": rojoSeg, "seg_verde": verdeSeg,
                "min_amarillo":amarilloMin, "hora_amarillo":amarilloHora,
                "dia": dia
                }

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


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)