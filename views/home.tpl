% rebase('base.tpl', title="Dispensador programable pruebas")
<h1>Pagina principal</h1>
<p>{{fecha}}</p>
<h3>Estado:</h3>

<table>
    <tr>
        <th>Contenedor</th>
        <th>Contenido</th>
        <th>Cargado</th>
    </tr>
<%
import random
medicina = ['Aspirina', 'Vitaminas']
%>
% for i in range(1, 7):
        <tr>
            <td>{{i}}</td>
            <td>{{random.choice(medicina)}}</td>
            <td>{{random.randint(0, 6)}} de 6</td>
        </tr>
% end
</table>