% rebase('base.tpl', title='Angulos')
<h1>Prueba Angulos servomotor</h1>
<form action="/angulos" method="POST">
    % for i in range(0, 190, 30):
        % if angulo == i:
            <input type="radio" name="angulo" value="{{i}}" checked>{{i}}
        % else:
            <input type="radio" name="angulo" value="{{i}}">{{i}}
        % end
    % end
    <input type="submit" name="submitBnt" value="Enviar">
</form>