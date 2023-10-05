const express = require('express');
const app = express();

// Configurar el directorio 'public' como carpeta de archivos estáticos
app.use(express.static('public'));

// Ruta de inicio que servirá 'index.html' desde la carpeta 'public'
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

const PORT = 3000; // Puerto en el que el servidor escuchará

app.listen(PORT, () => {
  console.log(`Servidor en ejecución en http://localhost:${PORT}`);
});
