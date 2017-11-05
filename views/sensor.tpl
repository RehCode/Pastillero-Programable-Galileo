% rebase('base.tpl', title='Sensor')
<h1>Sensor</h1>
<h2>Calibración</h2>
<form action="/sensor" method="POST">
    <label for="limiteLuz">Limite:</label>
    <input class="inDigitos" type="number" name="limiteLuz" id="limiteLuz" min="1" max="1010" value="{{sensor_limite}}" required>
    <input type="submit" value="Enviar">
</form>