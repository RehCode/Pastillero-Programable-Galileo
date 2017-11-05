% rebase('base.tpl', title='Login')
<h2>Administrador del sistema</h2>
<form action="/login" method="POST">
    <label for="usaurio">Usuario</label>
    <input type="text" id="usuario" name="usuario">
    </brb>
    <label for="password">Contraseña</label>
    <input type="password" name="password" id="password">
    </brb>
    <input type="submit" value="Ingresar">
    % if not ok_login:
        <p>usuario o contraseña incorrecto</p>
    % end
</form>

<!-- 
<form action="/login" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
</form> -->