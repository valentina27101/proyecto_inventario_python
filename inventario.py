from colorama import Fore, Back, Style, init
init () # Iniciar colorama para usar colores 
print(Fore.MAGENTA + "----------------------------")
# Mensaje de bienvenida 
print(Fore.MAGENTA+ "Bienvenido al inventario")
print(Fore.MAGENTA + "----------------------------")
print(Fore.MAGENTA)

# Solicita nombre del producto
while True:
   nombre = input("ingrese el nombre del producto: ")
# Revisa que solo tenga letras
   if nombre.replace(" ", "").isalpha():
       print("nombre válido.")
       break
   else:
       print("Error: solo se permiten letras.")

# Valida precio del producto 
while True:
    try:
        precio_unitario = float(input("ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: debe ingresar un precio válido.")
# Valida cantidad de productos
while True:
    try:
        cantidad = int(input("ingrese la cantidad de productos: "))
        break
    except ValueError:
        print("Error: debe ingresar una cantidad válida.")

# calcula costo total
costo_total = (precio_unitario * cantidad)

# Muestra resultados
print(Fore.MAGENTA + "----------------------------")
print(Fore.MAGENTA+ "factura")
print(Fore.MAGENTA + "----------------------------")
print("nombre del producto:", nombre) 
print("precio unitario:", precio_unitario)
print("cantidad:", cantidad)
print("costo total:", costo_total)

# Este programa permite registrar un producto en un inventario.
# Solicita al usuario el nombre del producto, precio y la cantidad.
# luego calcula el costo total multiplicando el precio por la cantidad
# y finalmente muestra la informacion en pantalla como una factura.
