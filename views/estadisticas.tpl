% rebase('base.tpl', title="Estadisticas")

<h1>Estadisticas</h1>
<table>
    <thead>
        <th>Nombre</th>
        <th>Contenedor</th>
        <th>Fecha</th>
        <th>Hora</th>
    </thead>
    <tbody>
        % for cont, nombre in enumerate(['Aspirina', 'Tratamiento espalda', 'Vitaminas']):
            % for hora in ['8:05', '12:03', '22:00']:
                <tr>
                    <td>{{nombre}}</td>
                    <td>{{cont + 1}}</td>
                    <td>2017-11-14</td>
                    <td>{{hora}}</td>
                </tr>
            % end
        % end
    </tbody>
</table>