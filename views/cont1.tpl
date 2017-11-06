% rebase('base.tpl', title="Contenedor #1")
<h2>Programacón</h2>
<form action="/cont1" method="POST">
    <label for="nombre">Descripción del contenido</label>
    <input type="text" name="nombre" id="nombre" value='{{cont1_nombre}}' required>
    <h2>Secciones</h2>

    <ol id='prog-cont'>
        % for seccion in cont1_secciones.keys():
            <li>
            <select name="{{seccion}}Dia">
                % for dia_nom in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
                    % if cont1_secciones[seccion]['dia'] == dia_nom:
                        <option value="{{dia_nom}}" selected>{{dia_nom}}</option>
                    % else:
                        <option value="{{dia_nom}}">{{dia_nom}}</option>
                    % end
                % end
            </select>
            <input class="inDigitos" type="number" name="{{seccion}}Hora" min="0" max="23" value="{{cont1_secciones[seccion]['hora']}}" required>Hrs
            <input class="inDigitos" type="number" name="{{seccion}}Min" min="0" max="60" value="{{cont1_secciones[seccion]['minuto']}}" required>Min
            </li>
        % end
        </ol>

    <input type="submit" value="Enviar">
</form>