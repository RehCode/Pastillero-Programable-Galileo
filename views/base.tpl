<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href='../static/css/base.css' rel='stylesheet' type='text/css'>
    <title>{{title or 'Pruebas'}}</title>
</head>
<body>
    <header>
        <h3>Dispensador programable pruebas</h3>
    </header>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/angulos">Angulos servo</a></li>
            <li><a href="/leds">Programacion leds</a></li>
            <li><a href="/sensor1">Sensor</a></li>
            <li><a href="/login">Login</a></li>
            <li><a href="/comentarios_ingreso">Comentarios</a></li>
        </ul>
    </nav>
    <section>
        
        {{!base}}

    </section>
    <footer>
        % from datetime import datetime
        <p>{{datetime.now().ctime()}}</p>
        <p>Prueba - Sensor, actuador y paginas</p>
    </footer>
</body>
</html>