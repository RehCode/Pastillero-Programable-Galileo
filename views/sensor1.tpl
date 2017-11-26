% rebase('base.tpl', title='Sensor')
<h1>Sensor #1</h1>
<h2>Calibración</h2>
<form action="/sensor1" method="POST">
    <label for="limiteLuz">Limite:</label>
    <input class="inDigitos" type="number" name="limiteLuz" id="limiteLuz" min="1" max="1010" value="{{sensor_limite}}" required>
    <input type="submit" value="Enviar">
</form>

<h2>Pastillas tomadas:</h2>

<table>
    <tr>
        <th>Pastilla</th>
        <th>Fecha</th>
    </tr>

% fecha = '2017-11-25 11:48:26'
% for i in range(1, 5):
        <tr>
            <td>{{i}}</td>
            <td>{{fecha}}</td>
        </tr>
% end
</table>