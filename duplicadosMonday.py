import json
import os
from collections import defaultdict

def buscarDuplicadosMonday(input_json_file, campo):
    try:
        # Obtener la ruta completa al archivo JSON de entrada
        input_json_path = os.path.abspath(input_json_file)

        # Leer los datos desde el archivo JSON
        with open(input_json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Crear un diccionario para contar las ocurrencias de cada valor en el campo especificado
        contador = defaultdict(int)

        # Encontrar registros duplicados en función del campo especificado
        duplicados = []

        # Contador de registros leídos
        registros_leidos = 0

        for registro in data:
            registros_leidos += 1
            valor_campo = registro.get(campo)
            if valor_campo is not None:
                contador[valor_campo] += 1
                if contador[valor_campo] > 1:
                    duplicados.append(registro)

        # Imprimir la cantidad de registros leídos
        print(f'Cantidad de registros leídos: {registros_leidos}')

        # Imprimir la cantidad de registros duplicados
        cantidad_duplicados = len(duplicados)
        print(f'Cantidad de registros duplicados en el campo "{campo}": {cantidad_duplicados}')

        # Guardar los registros duplicados en un nuevo archivo JSON
        output_json_file = 'duplicadosMonday.json'
        output_json_path = os.path.join(os.path.dirname(input_json_path), output_json_file)

        with open(output_json_path, 'w', encoding='utf-8') as output_json:
            json.dump(duplicados, output_json, ensure_ascii=False, indent=4)

        print(f'Se han encontrado y guardado los registros duplicados en "{output_json_file}".')

    except Exception as e:
        print(f'Error: {str(e)}')


# Uso de la función para buscar y guardar registros duplicados en "duplicadosMonday.json"
buscarDuplicadosMonday('c:\\ddbbClientes\output.json', "Name")  # Reemplaza 'Nombre' con el campo deseado
