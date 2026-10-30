# Importar Excel a MongoDB

Mini script en Python que lee un archivo Excel y guarda sus filas como documentos en MongoDB. Los títulos de la primera fila se utilizan como nombres de los campos.

## Requisitos

- Python 3.
- MongoDB en ejecución en `localhost:27017`.
- Un archivo `clientes.xlsx` en la misma carpeta que `importar.py`.

## Instalación

Instala las dependencias:

```bash
pip install openpyxl pymongo
```

## Formato del Excel

La primera fila debe contener los encabezados y los datos deben comenzar en la segunda fila. Utiliza encabezados únicos y sin celdas vacías.

Ejemplo:

| nombre | email | edad |
|--------|-------|------|
| Ana | ana@example.com | 28 |
| Luis | luis@example.com | 35 |

Cada fila se convierte en un documento como este:

```json
{
  "nombre": "Ana",
  "email": "ana@example.com",
  "edad": 28
}
```

MongoDB añade automáticamente el campo `_id`.

## Uso

1. Coloca `clientes.xlsx` en la misma carpeta que el script.
2. Asegúrate de que MongoDB está en ejecución.
3. Ejecuta:

```bash
python importar.py
```

El script lee la hoja activa del Excel, omite las filas completamente vacías e inserta los registros en:

- **Base de datos:** `prueba_excel`
- **Colección:** `clientes`

En la consola muestra los registros leídos y la cantidad de documentos insertados.

## Configuración

Puedes modificar estos valores en `importar.py`:

| Configuración | Valor predeterminado |
|---------------|----------------------|
| Archivo Excel | `clientes.xlsx` |
| URI de MongoDB | `mongodb://localhost:27017/` |
| Base de datos | `prueba_excel` |
| Colección | `clientes` |

## Consideraciones

- Cada ejecución inserta nuevos documentos; no actualiza registros existentes ni evita duplicados.
- El Excel debe contener al menos una fila con datos para realizar la inserción.
- Las fórmulas se leen usando el último resultado guardado por Excel; el script no las calcula.
