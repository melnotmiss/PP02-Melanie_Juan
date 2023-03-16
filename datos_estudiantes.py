import json


def datos_estudiantes():
    #Pedimos al usuario la cantidad de estudiantes
    estudiante = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))

    #Creamos un diccionario para almacenar la informacion de dichos estudiantes
    estudiantes = {}

    #Pedimos al usuario la informacion de cada estudiante para que esta sea añadida al diccionario
    for e in range(estudiante):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        matricula = input("Ingrese la matrícula del estudiante: ")
        estudiantes[nombre] = {"edad": edad, "matricula": matricula}

    #Guardamos el diccionario en un archivo llamado "estudiantes.json". Ya que el archivo no existe, el archivo se crea
    with open("estudiantes.json", "w") as file:
        json.dump(estudiantes, file)

    #Pedimos al usuario que nos de un nombre de un estudiante para buscarlo y leer el archivo que acabamos de crear
    #De esta forma conseguimos e imprimimos los datos del estudiante. De no estar en el archivo, entonces damos el 
    # mensaje de que el estudiante no fue registrado en nuestro archivo .json
    nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
    with open("estudiantes.json", "r") as file:
        estudiantes = json.load(file)
    if nombre in estudiantes:
        print("Nombre: {}".format(nombre))
        print("Edad: {}".format(estudiantes[nombre]["edad"]))
        print("Matrícula: {}".format(estudiantes[nombre]["matricula"]))
    else:
        print("No hay estudiantes con ese nombre.")

