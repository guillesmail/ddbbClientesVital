// Obtener una referencia al elemento <div> con la clase "resultados"
const resultadosDiv = document.querySelector('.mostrarResultados');

// Realizar una solicitud AJAX para cargar el archivo JSON
const xhr = new XMLHttpRequest();
xhr.open('GET', 'ddbb.json', true);

xhr.onload = function () {
  if (xhr.status === 200) {
    // Parsear el contenido del archivo JSON
    const data = JSON.parse(xhr.responseText);

    // Crear un contenedor para la tabla
    const tableContainer = document.createElement('div');
    tableContainer.className = 'tabla-container';

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

    // Agregar la tabla al contenedor
    tableContainer.appendChild(table);

    // Agregar el contenedor al div de resultados
    resultadosDiv.appendChild(tableContainer);
  } else {
    resultadosDiv.textContent = 'Error al cargar el archivo JSON.';
  }
};

xhr.send();
