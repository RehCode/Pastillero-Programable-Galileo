% rebase('base.tpl', title='Programacion de leds')
<h1>Programación temporal leds</h1>
<form action="/leds" method="POST">
    <p>
        <label for="rojo">Rojo</label>
        <input class="inDigitos" type="number" name="rojoSeg" id="rojo" min="1" max="60" value="{{rojo_seg}}" required>
        segundos
    </p>
    <p>
        <label for="verde">Verde</label>
        <input class="inDigitos" type="number" name="verdeSeg" id="verde" min="1" max="60" value="{{verde_seg}}" required>
        segundos
    </p>
    <p>
        <label>Amarillo</label>
        <ul style="list-style-type: none;">
            <li>
                Dia: 
                <select name="dia">
                    % for dia_nom in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
                        % if dia == dia_nom:
                            <option value="{{dia_nom}}" selected>{{dia_nom}}</option>
                        % else:
                        <option value="{{dia_nom}}">{{dia_nom}}</option>
                        % end
                    % end
                </select>
            </li>
            <li>
                Hora: <input class="inDigitos" type="number" name="amarilloHora" min="1" max="23" value="{{amarillo_hora}}" required>
            </li>
            <li>
                Minuto: <input class="inDigitos" type="number" name="amarilloMin" min="1" max="60" value="{{amarillo_min}}" required>
            </li>
        </ul>
    </p>
    <input type="submit" value="Enviar">
</form>
