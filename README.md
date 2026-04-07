# Programa De Inventario

## Descripción
Este programa es un sistema de inventario en consola que permite gestionar productos mediante operaciones CRUD (agregar, mostrar, buscar, actualizar y eliminar). Los datos se almacenan en una lista de diccionarios y el usuario puede interactuar con ellos a través de un menú. Además, el sistema calcula estadísticas del inventario y permite guardar y cargar la información en archivos CSV, asegurando validaciones y manejo de errores para evitar fallos durante su uso.

## Explicación del proyecto paso a paso
## Requisitos

- Python 3


 ### Instalación de Python
 ---
Antes de ejecutar el programa, necesitamos instalar Python, que es el lenguaje de programación con el que está hecho el proyecto.

---
##### Qué es Python? 
Python es un programa que permite escribir y ejecutar código en la computadora.

---
##### Como lo instalo?

Instala Python siguiendo estos pasos:

---
1. Ir a la página oficial de Python.
   
-  ```[Python - Página oficial](https://www.python.org)```

2. Hacer clic en Download Python para descargar el programa.Descargar la versión más reciente de Python 3. Después de descargar Python desde la página oficial, se descargará un archivo parecido a este:
   
-  ```python-3.x.x.exe```
 
3. Abrir el archivo que se descargó.

4. Marcar la opción “Add Python to PATH”.
  **Importante :** Si no se marca esa opción, la computadora no reconocerá el comando Python.

5. Hacer clic en “Install Now”.

6. Esperar a que termine la instalación.
   
Cuando termina la instalación, Python ya queda listo para usarse en el computador.


### Como abrir la terminal
Si es windowns (Windowns + R)
Si es Linux (ctrl + Alt + T) 

---
### Abrir el proyecto en la terminal
##### Como lo hago? 
para usar el programa sigue los siguientes pasos: 

1. Abrir la terminal.

2. Clonar el repositorio usando el siguiente comando:
    ```git clone URL_DEL_REPOSITORIO ```
    En este caso seria: 
    ```https://github.com/valentina27101/proyecto_inventario_python.git```

3. Después debemos movernos a la carpeta del proyecto con el comando:

    ```cd nombre_de_la_carpeta ```

4. Una vez dentro de la carpeta, ya podemos abrir el proyecto y trabajar con los archivos.

   ---

## Cómo Funciona 
 #🧾 ¿Cómo funciona el sistema?

Este programa es un sistema de inventario en consola que permite gestionar productos usando operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y además guardar o cargar la información en archivos CSV.

# 🔄 Flujo general del sistema

El programa inicia mostrando un menú principal con 9 opciones:

- Agregar producto
- Mostrar inventario
- Buscar producto
- Actualizar producto
- Eliminar producto
- Ver estadísticas
- Guardar en CSV
- Cargar desde CSV
- Salir

El sistema funciona dentro de un ciclo while, lo que permite que el usuario siga usando el programa hasta que elija la opción Salir.

Cada opción del menú dirige a una función específica que realiza una tarea sobre el inventario.

# 📦 Estructura del inventario

El inventario se maneja en memoria como una lista de diccionarios, donde cada producto tiene esta forma:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

Esto permite acceder fácilmente a los datos y modificarlos cuando sea necesario.

# ⚙️ Funcionalidades principales (CRUD)
Agregar producto:
Pide nombre, precio y cantidad, valida los datos y los guarda en el inventario.
Mostrar inventario:
Recorre la lista y muestra todos los productos con su información.
Buscar producto:
Busca por nombre y retorna el producto si existe o None si no lo encuentra.
Actualizar producto:
Permite cambiar el precio y/o la cantidad de un producto existente.
Eliminar producto:
Borra un producto del inventario según su nombre.

# 📊 Estadísticas del inventario

El sistema calcula automáticamente:

Unidades totales: suma de todas las cantidades
Valor total: suma de (precio × cantidad)
Producto más caro: el de mayor precio
Producto con mayor stock: el de mayor cantidad


# 💾 Guardar en CSV

Cuando el usuario selecciona guardar:

Se define una ruta (inventario.csv)
Se valida que el inventario no esté vacío

Se escribe el archivo con formato:
nombre,precio,cantidad
Si ocurre un error (permisos, escritura, etc.), se captura con try/except
Si todo sale bien, se muestra un mensaje confirmando el guardado

# 📂 Cargar desde CSV

El proceso de carga funciona así:

Se pide la ruta del archivo
Se valida que exista y tenga el formato correcto
Se revisa que:
Tenga encabezado válido
Cada fila tenga 3 columnas
precio sea float y cantidad int (no negativos)
Las filas inválidas se omiten y se cuenta cuántas fallaron

Luego el usuario decide:

Sobrescribir (S): reemplaza todo el inventario
Fusionar (N):
Si el producto ya existe: suma cantidades
Si el precio cambia: se actualiza al nuevo

Al final se muestra un resumen:

productos cargados
filas inválidas
acción realizada

# 🧠 Modularización del código

El programa está dividido en módulos para mejor organización:

app.py: contiene el menú principal y la interacción con el usuario
servicios.py: contiene las funciones CRUD y estadísticas
archivos.py: maneja guardar y cargar CSV


# 🔐 Validaciones y manejo de errores
Se valida que las opciones del menú sean entre 1 y 9
Se controla que precio y cantidad sean números y no negativos
Se usan try/except para evitar que el programa se cierre por errores
Siempre se muestran mensajes claros al usuario

## Diagrama de flujo

![alt text](diagrama_flujo.drawio)


## Estado

> Este proyecto está terminado.

## Autora
Valentina Pacheco Ortiz
