# Esta función sirve para agregar productos al inventario
def agregar_productos(inventario, nombre, precio_unitario, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto.
    precio_unitario (float): Precio del producto.
    cantidad (int): Cantidad disponible.

    Retorna:
    bool: True si el producto se agrega correctamente, False si hay error.
    """

    if not nombre or precio_unitario <= 0 or cantidad <= 0:
        return False
    
    #Verifica si el producto ya existe
    for prod in inventario:
        if prod["nombre"].lower() == nombre.lower():
            # Si existe, suma la cantidad
            prod["cantidad"] += cantidad
            prod["precio"] = precio_unitario
            return True
    
    # Creo el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio_unitario,
        "cantidad": cantidad 
    } 
    # Agrega el producto a la lista inventario
    inventario.append(producto)

    return True
  

# Esta función muestra todos los productos guardados
def mostrar_inventario(inventario):
    """
    Muestra todos los productos almacenados en el inventario.

    Parámetros:
    inventario (list): Lista de productos.

    Retorna:
    None
    """

    # Verifica si el inventario está vacío
    if not inventario:
        print("---El inventario esta vacío---")
        return
    print("-" * 45)
        # Recorre la lista y muestro cada producto
    for prod in inventario:
        print(f"Producto: {prod['nombre']} | Precio: {prod['precio']} | Cantidad: {prod['cantidad']}")

def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por su nombre.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a buscar.

    Retorna:
    dict: Producto encontrado.
    None: Si el producto no existe.
    """

    for prod in inventario:
        if prod["nombre"].lower() == nombre.lower():
            return prod
        
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a actualizar.
    nuevo_precio (float, opcional): Nuevo precio del producto.
    nueva_cantidad (int, opcional): Nueva cantidad del producto.

    Retorna:
    bool: True si se actualiza correctamente, False si no se encuentra el producto.
    """
     
    for prod in inventario:
        if prod ["nombre"].lower() == nombre.lower():
            print(f"Producto a actualizar:{prod['nombre']}")

            if nuevo_precio is not None:
                if nuevo_precio > 0:
                    prod["precio"] = nuevo_precio
            
            if nueva_cantidad is not None:
                if nueva_cantidad > 0:
                    prod["cantidad"] = nueva_cantidad

            return True
        
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto a eliminar.

    Retorna:
    Bool: True si se elimina, False si no se encuentra.
    """
    for prod in inventario:
        if prod ["nombre"].lower() == nombre.lower():
            print(f"Producto a eliminar: {prod['nombre']}")
            inventario.remove(prod)
            return True
    return False

    
# Esta función calcula estadísticas del inventario
def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Parámetros:
    inventario (list): Lista de productos.

    Retorna:
    dict: Contiene:
        - unidades_totales (int)
        - valor_total (float)
        - producto_mas_caro (tuple: nombre, precio)
        - producto_mayor_stock (tuple: nombre, cantidad)
    None: Si el inventario está vacío.
    """
    
    # Verifica si el inventario está vacío
    if not inventario:
        return None

    # Lambda para calcular subtotal por producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Total de unidades
    unidades_totales = sum(p["cantidad"] for p in inventario)

    # Valor total del inventario
    valor_total = sum(subtotal(p) for p in inventario)

    # Producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])

    # Producto con mayor cantidad
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }



