// Obtener una referencia al elemento <div> con la clase "resultados"
const resultadosDiv = document.querySelector('.mostrarResultados');

// Realizar una solicitud AJAX para cargar el archivo JSON
const xhr = new XMLHttpRequest();
xhr.open('GET', 'ddbb.json', true);

xhr.onload = function () {
  if (xhr.status === 200) {
    // Parsear el contenido del archivo JSON
    const data = JSON.parse(xhr.responseText);

    // Crear una tabla HTML
    const table = document.createElement('table');

    // Crear la cabecera de la tabla
    const headerRow = document.createElement('tr');
    for (const key in data[0]) {
      if (data[0].hasOwnProperty(key)) {
        const th = document.createElement('th');
        th.textContent = key;
        headerRow.appendChild(th);
      }
    }
    table.appendChild(headerRow);

    // Crear filas para cada cliente
    data.forEach(function (cliente) {
      const row = document.createElement('tr');
      for (const key in cliente) {
        if (cliente.hasOwnProperty(key)) {
          const cell = document.createElement('td');
          cell.textContent = cliente[key];
          row.appendChild(cell);
        }
      }
      table.appendChild(row);
    });

    // Agregar la tabla al div de resultados
    resultadosDiv.appendChild(table);
  } else {
    resultadosDiv.textContent = 'Error al cargar el archivo JSON.';
  }
};

xhr.send();

// ... (código anterior)

// Agregar estilos CSS en línea
table.style.borderCollapse = 'collapse';
table.style.width = '100%';
table.style.border = '1px solid #ddd';

// Aplicar estilos a las celdas (th y td)
const cells = table.querySelectorAll('th, td');
cells.forEach(function (cell) {
  cell.style.padding = '8px';
  cell.style.border = '1px solid #ddd';
});

// Estilos para la fila de encabezado (cabecera de la tabla)
headerRow.style.backgroundColor = '#f2f2f2';

// Estilos para las filas impares
const rows = table.querySelectorAll('tr:nth-child(odd)');
rows.forEach(function (row) {
  row.style.backgroundColor = '#f9f9f9';
});

// Estilos para las filas pares
const evenRows = table.querySelectorAll('tr:nth-child(even)');
evenRows.forEach(function (row) {
  row.style.backgroundColor = '#fff';
});

// Agregar la tabla al div de resultados
resultadosDiv.appendChild(table);

// ...

