% rebase('base.tpl')
<h1>Angulos servomotor</h1>
<form action="/angulos" method="POST">
    <input type="radio" name="angulo" id="0"> 0
    <input type="radio" name="angulo" id="30"> 30
    <input type="radio" name="angulo" id="60"> 60
    <input type="radio" name="angulo" id="90"> 90
    <input type="radio" name="angulo" id="120"> 120
    <input type="radio" name="angulo" id="160"> 160
    <input type="radio" name="angulo" id="180"> 180
    <input type="submit" name="submitBnt" value="Enviar">
</form>