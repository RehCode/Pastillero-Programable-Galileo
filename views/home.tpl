% rebase('base.tpl', title="Dispensador programable pruebas")
<h1>Inicio</h1>
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
medicina = ['Aspirina', 'Vitamina B']
%>
% for i in range(1, 8):
        <tr>
            <td>{{i}}</td>
            <td>{{random.choice(medicina)}}</td>
            <td>{{random.randint(0, 7)}} de 7</td>
        </tr>
        % end
</table>