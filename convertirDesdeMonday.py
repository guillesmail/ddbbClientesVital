import pandas as pd
import json
import os

def excel_to_json(input_excel_file, output_json_file, columns_to_show=None):
    try:
        # Obtener la ruta completa al archivo de Excel
        excel_file_path = os.path.abspath(input_excel_file)
        # Leer el archivo Excel
        df = pd.read_excel(excel_file_path)

        # Reemplazar NaN por ""
        df.fillna("", inplace=True)

        # Filtrar el DataFrame para mostrar solo las columnas especificadas
        if columns_to_show:
            df = df[columns_to_show]
            
        # Separar la columna "Name" en "Nombre" y "Apellido"
        if 'Full Name' in df.columns:
            df[['nombre', 'apellido']] = df['Full Name'].str.split(n=1, expand=True)

            # Capitalizar la primera letra de cada palabra en "Nombre" y "Apellido"
            df['nombre'] = df['nombre'].str.title()
            df['apellido'] = df['apellido'].str.title()
            
        # Capitalizar la primera letra de cada palabra en la columna "Name"
        if 'Full Name' in df.columns:
            df['Full Name'] = df['Full Name'].str.title()


        # Convertir el DataFrame a una lista de diccionarios
        data = df.to_dict(orient='records')

        # Obtener la ruta de la carpeta del archivo de entrada
        input_folder = os.path.dirname(excel_file_path)

        # Construir la ruta completa al archivo JSON de salida en la misma carpeta
        json_file_path = os.path.join(input_folder, output_json_file)
       
        # Guardar los datos en un archivo JSON
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        print(f'El archivo JSON "{output_json_file}" se ha creado en la misma carpeta que el archivo de entrada.')

    except Exception as e:
        print(f'Error: {str(e)}')

# Uso de la función para crear "exportMonday.txt" en la misma carpeta que "monday.xlsx"
# Especifica las columnas que deseas mostrar en el archivo HTML (puedes ajustar esta lista)
# columnas_a_mostrar = ['Name', 'RUBROS INTERES', 'EMAIL', 'Teléfono', 'LOCALIDAD']
columnas_a_mostrar = []
excel_to_json('C:\\ddbbClientes\exportBitrix.xlsx', 'C:\\ddbbClientes\ContactosBitrix24.json',columns_to_show=columnas_a_mostrar)

# Uso de la función
# excel_to_json('c:\\ddbbClientes\monday.xlsx', 'c:\\ddbbClientes\output.json')
