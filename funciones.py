# Lista donde se guardan todos los productos del inventario
inventario = []

# Esta función sirve para agregar productos al inventario
def agregar_productos():
    
    
    # Valida nombre del producto    
    while True:
        nombre = input("ingrese el nombre del producto: ")
        # Revisa que solo tenga letras
        if nombre.replace(" ", "").isalpha() or len(nombre) == 0:
            print("nombre válido.")
            break
        else:
            print("Error: solo se permiten letras.")

    # Valida que el precio sea un número válido 
    while True:
        try:
            precio_unitario = float(input("ingrese el precio del producto: "))
            
            if precio_unitario <= 0:
                print("Error: debe ser mayor que 0.")
            else:
                break

        except ValueError:
            print("Error: debe ingresar un precio válido.")

    # Valida que la cantidad sea un número válido
    while True:
        try:
            cantidad = int(input("ingrese la cantidad de productos: "))
            
            if cantidad <= 0:
                print("Error: debe ser mayor que 0.")
            else:
                break
            
        except ValueError:
            print("Error: debe ingresar una cantidad válida.")

    # Creo el producto como diccionario
    productos = {
        "nombre": nombre,
        "precio": precio_unitario,
        "cantidad": cantidad 
    } 
    # Agrega el producto a la lista inventario
    inventario.append(productos)
    print("el producto fue agregado") 
    return inventario
  

# Esta función muestra todos los productos guardados
def mostrar_inventario():

    # Verifica si el inventario está vacío
    if not inventario:
        print("El inventario esta vacío")
    else:
        print("Inventario: ")

        # Recorre la lista y muestro cada producto
        for prod in inventario:
            print(f"Producto: {prod['nombre']} | Precio: {prod['precio']} | Cantidad: {prod['cantidad']}")

# Esta función calcula estadísticas del inventario
def calculo_estadisticas():
    
    # Variables para guardar los resultados
    valor_total = 0
    cantidad_total = 0

    # Recorre los productos para calcular el total
    for prod in inventario:
        precio = prod["precio"]
        cantidad = prod["cantidad"]

        valor_total += precio * cantidad
        cantidad_total += cantidad
    # Muestra los resultados
    print("\n===Estadísticas===")
    print(f"el valor del inventario es: {valor_total}")
    print(f"la cantidad total de productos registrados es: {cantidad_total}")

# Este programa permite gestionar un inventario básico.
# Se pueden agregar productos, ver el inventario y calcular estadísticas.
# Se usaron listas, diccionarios, ciclos y condicionales.
