import pandas as pd
import json
import os

def excel_to_json(input_excel_file, output_json_file, columns_to_show=None):
    try:
        # Obtener la ruta completa al archivo de Excel
        excel_file_path = os.path.abspath(input_excel_file)
         # print(excel_file_path)
        # Leer el archivo Excel
        df = pd.read_excel(excel_file_path)

        # Reemplazar NaN por ""
         # df.fillna("", inplace=True)

        # Filtrar el DataFrame para mostrar solo las columnas especificadas
        if columns_to_show:
            df = df[columns_to_show]
            
        # Convertir el DataFrame a una lista de diccionarios
        data = df.to_dict(orient='records')

        # Editar el valor de la clave "Phone" en cada diccionario según las consignas
        for entry in data:
            phone_number = str(entry.get("Phone", ""))  # Convertir a cadena y obtener el valor actual de "Phone"
            
            # 3. Quitar todos los espacios vacíos " "
            phone_number = phone_number.replace(" ", "")
            
            # 1. Quitar el signo "-"
            phone_number = phone_number.replace("-", "")

            # 2. Si no empieza con +549, agregarlo
            if not phone_number.startswith("549") and not phone_number.startswith("+549"):
                phone_number = "+549" + phone_number
                    
            # Actualizar el valor de "Phone" en el diccionario
            entry["Phone"] = phone_number

        # Obtener la ruta de la carpeta del archivo de entrada
        input_folder = os.path.dirname(excel_file_path)

        # Construir la ruta completa al archivo JSON de salida en la misma carpeta
        json_file_path = os.path.join(input_folder, output_json_file)
       
        # Guardar los datos en un archivo JSON
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=1)

        print(f'El archivo JSON "{output_json_file}" se ha creado en la misma carpeta que el archivo de entrada.')
        
        
    except Exception as e:
        print(f'Error: {str(e)}')


columnas_a_mostrar = []
excel_to_json('C:\ddbbClientes\contactosCELwappbkp\importarCEL.xlsx', 'C:\ddbbClientes\contactosCELwappbkp\importarCEL.json',columns_to_show=columnas_a_mostrar)

# Uso de la función
# excel_to_json('c:\\ddbbClientes\monday.xlsx', 'c:\\ddbbClientes\output.json')
