# Importo las funciones necesarias
from menu import mostrar_menu
from funciones import agregar_productos, mostrar_inventario, calculo_estadisticas
from limpiar_pantalla import deleteScreen, pauseScreen
# Esta es la función principal que controla el programa
def main():

    # Este ciclo mantiene el programa ejecutándose hasta que el usuario decida salir
    while True:
        # Muestra el menú
        deleteScreen()

        mostrar_menu()
       
        # Pide la opción al usuario
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            agregar_productos()
            pauseScreen()

        elif opcion == "2":
            mostrar_inventario()
            pauseScreen()

        elif opcion == "3":
            calculo_estadisticas()
            pauseScreen()

        elif opcion == "4":
            print("==Gracias por utilizar el inventario==")
            break

        else:
            print("Opción inválida")
                  
main()

# Este programa permite gestionar un inventario básico.
# El usuario puede agregar productos, ver el inventario
# y calcular estadísticas como el valor total y la cantidad.
# Se utilizaron condicionales, bucles, listas y diccionarios.
