from pathlib import Path
from openpyxl import load_workbook
from pymongo import MongoClient

#Buscamos en la misma carpeta en la que estamos un fichero con el nombre indicado
ruta_excel = Path(__file__).parent / "clientes.xlsx"

libro = load_workbook(ruta_excel, data_only=True)
hoja = libro.active

# Definimos que la primera fila es la de títulos y que los datos empiezan en la segunda fila
encabezados = [celda.value for celda in hoja[1]]
registros = []

for fila in hoja.iter_rows(min_row=2, values_only=True):
    if all(valor is None for valor in fila):
        continue  # Saltar filas vacías

    # Creamos un diccionario para cada fila, combinando los encabezados con los valores de la fila
    registros.append(dict(zip(encabezados, fila)))

print(f"Se han importado {len(registros)} registros desde el archivo Excel.")

print(registros)  # Imprimimos los registros importados para verificar

# Conectamos a la base de datos MongoDB
with MongoClient("mongodb://localhost:27017/") as cliente:
    coleccion = cliente["prueba_excel"]["clientes"]
    resultado = coleccion.insert_many(registros)
    print(f"Se han insertado {len(resultado.inserted_ids)} registros en la base de datos MongoDB.")