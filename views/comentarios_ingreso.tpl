% rebase('base.tpl', title="Ingreso de comentarios")
<h1>Ingreso de comentarios</h1>
<form action="/com_trat" method="POST">
    <h2>Tratamiento</h2>
    <textarea name="tratamientocom" id="tratamientocom" cols="30" rows="5"></textarea>
    <br>
    <input type="submit" value="Enviar">    
</form>

<form action="/com_cont" method="POST">

    <h2>Por contenedor</h2>
    <select name="contenedor">
        % for cont in range(1, 8):
            <option value="{{cont}}">#{{cont}}</option>
        % end
    </select>
    <br>
    <textarea name="comcont" id="comcont" cols="30" rows="5"></textarea>
    <br> 
    <input type="submit" value="Enviar">
</form>