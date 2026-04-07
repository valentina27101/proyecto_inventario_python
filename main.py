# Importo las funciones necesarias
from menu import mostrar_menu
from servicios import agregar_productos, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv
from limpiar_pantalla import deleteScreen, pauseScreen

# Esta es la función principal que controla el programa
def main():
    # Lista donde se guardan todos los productos del inventario
    inventario = []
    # Este ciclo mantiene el programa ejecutándose hasta que el usuario decida salir
    while True:
        deleteScreen()
       
        # Muestra el menú
        mostrar_menu()
        opcion = input("seleccione una opción: ")
        if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Opción inválida.Ingrese un número del 1 al 9.")
            pauseScreen()
            continue
            
        # Pide la opción al usuario
        try:
            if opcion == "1":
                print("\n--- Agregar Producto ---")
                while True:
                    nombre = input("ingrese el nombre del producto: ")
                    
                    # Revisa que solo tenga letras
                    if not nombre.replace(" ", "").isalpha() or len(nombre) == 0:
                        print("Error: solo se permiten letras.")
                        continue
                    
                    else:
                        print("nombre válido")
                        break
                
                while True:
                    try:
                        precio_unitario = float(input("ingrese el precio del producto: "))
                        if precio_unitario <= 0:
                            print("Error: debe ser mayor que 0.")   
                        else:
                            break
                    except ValueError:
                        print("Error: debe ingresar un precio válido.")
            
                while True:
                    try:
                        cantidad = int(input("ingrese la cantidad de productos: "))
                        if cantidad <= 0:
                            print("Error: debe ser mayor que 0.")
                        else:
                            break
                    
                    except ValueError:
                        print("Error: debe ingresar una cantidad válida.")

                agregar_productos(inventario, nombre, precio_unitario, cantidad)
                    
                pauseScreen()
            
            elif opcion == "2":
                print("\n--- Inventario ---")
                mostrar_inventario(inventario)
                pauseScreen()
            
            elif opcion == "3":
                print("\n--- Buscar Producto ---")
                nombre = input("Ingrese el nombre del producto a buscar: ")
                resultado = buscar_producto(inventario, nombre)

                if resultado:
                    print(f"Encontrado: {resultado['nombre']}| Precio: {resultado['precio']} | Cantidad: {resultado['cantidad']}")
            
                else:
                    print("producto no encontrado")
                pauseScreen()

            elif opcion == "4":
                print("\n--- Actualizar Producto ---")
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                
                while True:
                    precio = input("Ingrese el precio del producto a actualizar:  ")
                    
                    if precio == "":
                        nuevo_precio = None
                        break
                    
                    try:
                        nuevo_precio = float(precio)
                        if nuevo_precio <= 0:
                            print("Error: el precio debe ser mayor que 0")
                        else:
                            break
                    except ValueError:
                        print("Error: ingrese un precio válido")
                        

                while True:
                    cantidad = input("Ingrese la cantidad del producto a actualizar: ")
                    if cantidad == "":
                        nueva_cantidad = None
                        break
        
                    try:
                        nueva_cantidad = int(cantidad)
                        if nueva_cantidad <= 0:
                            print("Error: debe ser mayor que 0")
                        else:
                            break
                    except ValueError:
                        print("Error: ingrese una cantidad válida")
                        
                if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                    print("Producto actualizado")
                else:
                    print("Producto no encontrado")

                pauseScreen()

            elif opcion == "5": 
                print("\n--- Eliminar Producto ---")
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                
                if eliminar_producto(inventario, nombre):
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")
                pauseScreen()
                
            elif opcion == "6":
                print("\n--- Estadísticas ---")
                stats = calcular_estadisticas(inventario)

                if stats:
                    print(f"Unidades totales: {stats['unidades_totales']}")
                    print(f"Valor total: {stats['valor_total']}")
                    print(f"Producto más caro: {stats['producto_mas_caro'][0]} (${stats['producto_mas_caro'][1]})")
                    print(f"Mayor stock: {stats['producto_mayor_stock'][0]} ({stats['producto_mayor_stock'][1]} unidades)")
                else:
                    print("Inventario vacío")

                pauseScreen()
                
            elif opcion == "7":
                print("\n--- Guardar CSV ---")
                ruta = "inventario.csv"
                guardar_csv(inventario, ruta)
                    
                pauseScreen()

            elif opcion == "8":
                ruta = "inventario.csv"
                productos, errores = cargar_csv(ruta)

                if productos is None:
                    print("No se pudo cargar el archivo.")
                    pauseScreen()
                    continue

                sobrescribir_fusionar = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                        
                if sobrescribir_fusionar == "S":
                    inventario.clear()
                    inventario.extend(productos)
                    print("[*] Inventario reemplazado.")

                elif sobrescribir_fusionar == "N":
                    # Fusión: Busca si existe para sumar o añade si es nuevo
                    for producto in productos:
                        existe = buscar_producto(inventario, producto["nombre"])
                                
                        if existe:
                            existe["cantidad"] += producto["cantidad"]
                            existe["precio"] = producto["precio"]
                                
                        else:
                            inventario.append(producto)
                            
                    print("[*] Inventario fusionado (política: sumar stock/actualizar precio).")
                else:
                    print("Opción inválida") 
                    pauseScreen()
                    continue
                    
                print("\n=== Resumen de carga ===")
                print(f"Productos cargados: {len(productos)}")
                print(f"Filas inválidas: {errores}")
                pauseScreen()
                        
            elif opcion == "9":
                print("Saliendo del sistema...")
                break

            else:
                print("Opcion inválida.")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos y no negativos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")          

main()


            
