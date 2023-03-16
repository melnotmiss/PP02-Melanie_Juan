#Melanie y Juan 
#21-0949 y 21-0041

#Se requiere desarrollar un programa modular que realice lo siguiente:

#1. Comida por categoría. Leer el archivo adjunto "wendys-menu.csv", y devolver el promedio de las calorías de 
# los alimentos agrupados por categorías.

#2. Datos estudiantes. Preguntar al usuario la cantidad de estudiantes que desea ingresar. 
#Para cada estudiante, solicitar su nombre, edad y matrícula. Guardar esta información en un archivo llamado 
# "estudiantes.json" usando un diccionario, donde el nombre del estudiante es la clave y la edad y grado son valores. 
#Solicitar por teclado el nombre de un estudiante y leer el archivo "estudiantes.json" para imprimir el detalle de 
# ese estudiante. Si el estudiante no está en el archivo, devolver el mensaje: "No hay estudiantes con ese nombre".

#Importamos ambos módulos
import comida_categoria
import datos_estudiantes

#Definimos la funcion de nuestro de menu de opciones
def menu_opciones():
    #Presentamos las opciones al usuario
    print("Menú de opciones\n1.Comida por categoría\n2.Datos estudiantes")
    opcion = int(input("A qué módulo desea acceder?: "))
    if opcion == 1:
        #De seleccionar la opcion "2", corremos el primer modulo 
        comida_categoria.comida_categoria()
    elif opcion == 2:
        #De seleccionar la opcion "2", corremos el segundo modulo 
        datos_estudiantes.datos_estudiantes()
        #De no haber seleccionado ninguna de las anteriores, la seleccion no seria valida, por lo tanto imprimimos
        # "La opcion ingresada no es valida"
    else:
        ("La opción ingresada no es válida")

menu_opciones()