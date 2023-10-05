from pymongo import MongoClient
import socket
import json

# Intenta configurar la conexión a MongoDB
try:
    client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=2000)
    db = client.clientesDDBB
    collection = db.monday  # Aquí define 'monday' como el nombre de la colección

    # Comprueba si la conexión se estableció correctamente
    server_info = client.server_info()
    print("Conexión a MongoDB CORRECTA.")
    
    # Define una consulta con una expresión regular
    regex_query = {
        "nombre": {
            "$regex": "Calvi",  # Expresión regular para buscar
        }
    }

    # Realiza una consulta a la colección
    data = list(collection.find(regex_query))
    
    

    # Imprime los resultados en formato JSON
    for document in data:
        # Convertir ObjectId a cadena antes de incluirlo en el documento JSON
        document["_id"] = str(document["_id"])
        print(json.dumps(document, indent=4))
        print("\n")
       
    # Obtiene la cantidad total de registros en la colección
    total_records = collection.count_documents({})

    # Imprime la cantidad de registros leídos y la cantidad de registros encontrados
    len_data = len(data)
    print(f"Registros Encontrados: {len_data}")  # Corregido de 'result' a 'data'
    print(f"Registros Leidos: {total_records}")
    
    
    # Imprime los resultados como una cadena JSON
     #print(json.dumps({
      #   "data": data,
     #    "total_records": total_records,
     #    "len_data": len(data)
   #  }))

    
    # Cierra la conexión a MongoDB
    client.close()
except socket.timeout as timeout_err:
    print(f"Timeout: {timeout_err}")
except Exception as e:
    # Captura cualquier otra excepción y muestra un mensaje de error
    print(f"Error al conectarse a MongoDB: {e}")
