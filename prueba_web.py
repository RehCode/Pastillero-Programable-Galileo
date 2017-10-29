import time
import threading
from datetime import datetime
from bottle import route, run, template, request, redirect

# import mraa

# print(mraa.getVersion())

# pin13 = mraa.Gpio(13)
# pin13.dir(mraa.DIR_OUT)

# pin12 = mraa.Gpio(12)
# pin12.dir(mraa.DIR_OUT)

# pin13.write(0)
# pin12.write(0)

led_boton_web_encendido = False
led_fecha_encendido = False
continuar = True

def hilo():
    global continuar
    while True:

        if continuar:
            ahora = datetime.today()
            if ahora.second % 5 == 0:
                print(ahora.ctime(), ahora.second)
                led_fecha_encendido

        time.sleep(1)

@route('/')
def raiz():
    return "Hola desde Intel galileo"


@route('/encenderpin/<numpin:int>')
def encender(numpin):
    return template('Encendiendo pin {{numpin}}...', numpin=numpin)


@route('/fecha')
def fecha():
    return datetime.now().ctime()

@route('/on')
def on_led():
    global continuar
    # pin13.write(1)
    continuar = True
    return 'Encendido!'

@route('/off')
def on_led():
    global continuar
    # pin13.write(0)
    continuar = False
    return 'Apagado!'



@route('/boton')
def boton():
    return '''
    <form action="/boton" method="post">
        <button type="submit" name="push">Push!</button>
    </form>
    '''

@route('/boton', method='POST')
def accion():
    global led_boton_web_encendido
    print("Boton presionado")
    led_boton_web_encendido = not led_boton_web_encendido

    if led_boton_web_encendido:
        # pin12.write(1)
        print("PRENDIDO")
    else:
        # pin12.write(0)
        print("Apagado")

    print("valor: ", led_boton_web_encendido)
    redirect('/boton')


@route('/login')
def forma():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


def check_login(username, password):
    if username == 'rene' and password == '123':
        return True
    else:
        return False


@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


if __name__ == '__main__':

    t = threading.Thread(target=hilo, daemon=True)
    t.start()
    run(host='0.0.0.0', port=8080, debug=True)
    continuar = False
