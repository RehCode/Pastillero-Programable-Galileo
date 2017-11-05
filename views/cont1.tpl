% rebase('base.tpl', title="Contenedor #1")
<h2>Programacón</h2>
<form action="/cont1" method="POST">
    <label for="nombre">Descripción del contenido</label>
    <input type="text" name="nombre" id="nombre" value='Sin nombre' required>
    <p>
        <h2>Secciones</h2>
        <label>#1</label>
        <select name="dia">
            % for dia_nom in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
            % if cont1_dia == dia_nom:
            <option value="{{dia_nom}}" selected>{{dia_nom}}</option>
            % else:
            <option value="{{dia_nom}}">{{dia_nom}}</option>
            % end
            % end
        </select>
        <input class="inDigitos" type="number" name="cont1Hora" min="1" max="23" value="{{cont1_hora}}" required>Hrs
        <input class="inDigitos" type="number" name="cont1Min" min="1" max="60" value="{{cont1_min}}" required>Min
    </p>
        
    <ol id='prog-cont'>
    % for mock in range(2, 8):
        <li>
        <select name="dia">
            % for dia_nom in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
                <option value="{{dia_nom}}">{{dia_nom}}</option>
            % end
        </select>
        <input class="inDigitos" type="number" name="cont{{mock}}Hora" min="1" max="23" value="14" required>Hrs
        <input class="inDigitos" type="number" name="cont{{mock}}Min" min="1" max="60" value="30" required>Min
        </li>
    % end
    </ol>

    <input type="submit" value="Enviar">
</form>