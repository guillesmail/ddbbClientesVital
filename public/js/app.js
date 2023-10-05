// Obtener una referencia al elemento <div> con la clase "resultados"
const resultadosDiv = document.querySelector('.mostrarResultados');

// Realizar una solicitud AJAX para cargar el archivo JSON
const xhr = new XMLHttpRequest();
// xhr.open('GET', 'ddbb.json', true);

data = [
  {
    "Nombre": "Armando",
    "Apellido": "Rosales",
    "Teléfono": 5492966639163.0,
    "email": "armando_rosales28@hotmail.com",
    "CIUDAD": "Sargento Vidal",
    "SUCURSAL": "",
    "ETIQUETAS": "Piscinas compra"
},
{
    "Nombre": "federico",
    "Apellido": "rafico",
    "Teléfono": 5492995312628.0,
    "email": "",
    "CIUDAD": "",
    "SUCURSAL": "",
    "ETIQUETAS": ""
},
{
    "Nombre": "Estefania",
    "Apellido": "Reyes",
    "Teléfono": 5492995243627.0,
    "email": "Stefaniacristelreyes@gmail.com",
    "CIUDAD": "Neuquén",
    "SUCURSAL": "",
    "ETIQUETAS": "Piscinas compra"
}
]

// xhr.onload = function () {
  function mostrarResultados() {
  if (xhr.status === 200) {
    // Parsear el contenido del archivo JSON
    //const data = JSON.parse(xhr.responseText);

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
mostrarResultados(data)
//xhr.send();

/* 

// Ejecuta el script Python y captura su salida
exec('python consulta_mongodb.py', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Error: ${stderr}`);
    return;
  }

  // Analiza la salida JSON del script Python
  const result = JSON.parse(stdout);

  // Accede a los datos que necesitas en JavaScript
  const data = result.data;
  const totalRecords = result.total_records;
  const lenData = result.len_data;

  // Usa los datos como desees en tu proyecto Node.js
  console.log("Data:", data);
  console.log("Total Records:", totalRecords);
  console.log("Length of Data:", lenData);
});

 */

/* ***************** js que recibe json desde python ******************

const { exec } = require('child_process');

exec('python tu_script.py', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Error: ${stderr}`);
    return;
  }
  const data = JSON.parse(stdout);
  // Ahora 'data' contiene los datos obtenidos de MongoDB.
  console.log(data);
});

******************************************************************** */