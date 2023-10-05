import pandas as pd
import json
import os

def excel_a_json_y_excel(archivo_excel_entrada, archivo_json_salida, archivo_excel_salida, columnas_a_mostrar=None):
    try:
        # Obtener la ruta completa al archivo de Excel
        ruta_archivo_excel = os.path.abspath(archivo_excel_entrada)
        
        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo_excel)

        # Filtrar el DataFrame para mostrar solo las columnas especificadas
        if columnas_a_mostrar:
            df = df[columnas_a_mostrar]

        # Editar el valor de la clave "Phone" en cada diccionario según las consignas
        for columna in df.columns:
            if columna == "Phone":
                df[columna] = df[columna].apply(lambda x: str(x).replace(" ", "").replace("-", ""))
                df[columna] = df[columna].apply(lambda x: "+549" + x if not x.startswith("+549") and not x.startswith("549") else x)
        
        # Obtener la ruta de la carpeta del archivo de entrada
        carpeta_entrada = os.path.dirname(ruta_archivo_excel)

        # Construir la ruta completa al archivo JSON de salida en la misma carpeta
        ruta_archivo_json = os.path.join(carpeta_entrada, archivo_json_salida)

        # Construir la ruta completa al archivo Excel de salida en la misma carpeta
        ruta_archivo_excel_salida = os.path.join(carpeta_entrada, archivo_excel_salida)

        # Guardar los datos en un archivo JSON
        with open(ruta_archivo_json, 'w', encoding='utf-8') as archivo_json:
            json.dump(df.to_dict(orient='records'), archivo_json, ensure_ascii=False, indent=1)

        # Guardar los datos en un archivo Excel
        df.to_excel(ruta_archivo_excel_salida, index=False)

        print(f'Los archivos JSON "{archivo_json_salida}" y Excel "{archivo_excel_salida}" se han creado en la misma carpeta que el archivo de entrada.')

    except Exception as e:
        print(f'Error: {str(e)}')

# Uso de la función
columnas_a_mostrar = []  # Define las columnas a mostrar en el archivo Excel
excel_a_json_y_excel('C:\ddbbClientes\contactosCELwappbkp\importarCEL.xlsx',
                    'C:\ddbbClientes\contactosCELwappbkp\importarCEL.json',
                    'C:\ddbbClientes\contactosCELwappbkp\importarCEL_output.xlsx',
                    columnas_a_mostrar)
