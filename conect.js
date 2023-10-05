const { exec } = require('child_process');

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
