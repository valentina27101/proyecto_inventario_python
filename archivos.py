import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
    inventario (list): Lista de productos.
    ruta (str): Ruta del archivo CSV.
    incluir_header (bool): Indica si se incluye el encabezado.

    Retorna:
    None
    """
    if not inventario:
        print("El inventario está vacío. No hay nada que guardar.")
        return

    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(archivo, fieldnames=campos)

            if incluir_header:
                writer.writeheader()

            writer.writerows(inventario)

        print(f"[*] Inventario guardado en: {ruta}")
    except PermissionError:
        print(f"Error: No se puede escribir en {ruta}. Cierra el archivo si está abierto.")
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV validando su estructura.

    Parámetros:
    ruta (str): Ruta del archivo CSV.

    Retorna:
    tuple:
        - list: Lista de productos válidos.
        - int: Cantidad de filas inválidas encontradas.

    Retorna (None, 0) si ocurre un error.
    """
    productos_cargados = []
    errores = 0
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            if [campo.strip().lower() for campo in reader.fieldnames] != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el encabezado correcto.")
                return None, 0

            for fila in reader:
                try:
                    # Obtener y validar datos
                    nombre = fila["nombre"].strip()
                    if not nombre:
                        raise ValueError

                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    if precio < 0 or cantidad < 0: 
                        raise ValueError
                    
                    productos_cargados.append({
                        "nombre": nombre, "precio": precio, "cantidad": cantidad
                    })
                except (ValueError, KeyError):
                    errores += 1

            return productos_cargados, errores
    
    except FileNotFoundError:
        print("[!] El archivo no existe.")
    except UnicodeDecodeError:
        print("[!] problema de codificación del archivo.")
    except Exception as e:
        print(f"[!] Error al cargar: {e}") 

    return None, errores
