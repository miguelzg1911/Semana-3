# Objetivo:

# Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.
# Instrucciones:

#     Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores 
#     sean otro diccionario con las claves edad y calificacion.

#     El programa debe permitir al usuario realizar las siguientes operaciones:
#         Agregar un nuevo estudiante (nombre, edad, calificación).
#         Modificar la calificación de un estudiante.
#         Mostrar la información de todos los estudiantes.
#         Eliminar un estudiante por su nombre.

print("\n""---Bienvenid@ al menu---""\n"
    "Aca puede llevar el registro de los estudiantes:")

Estudiantes = {}

def Agregar_Estud():
    nombre = input("\n""Ingresa el nombre del estudiante: ").lower()
    edad = int(input("Ingresa la edad del estudiante: "))
    calificacion = float(input(f"Ingresa la calificacion de {nombre}: "))
    Estudiantes[nombre] = {"edad": edad, "calificacion": calificacion}
    print(f"--Estudiante {nombre.capitalize()}, fue agregado con exito!--")

def Mod_Estud():
    nombre = input("\n""Ingresa el nombre del estudiante que deseas cambiarle la calificacion: ").lower()
    if nombre in Estudiantes:
        calificacion_nueva = float(input(f"Ingresa la nueva calificacion de {nombre}: "))
        Estudiantes[nombre]["calificacion"] = calificacion_nueva
        print(f"La calificacion de {nombre.capitalize()} a sido cambiada: {calificacion_nueva}")
    else:
        print("Ese estudiante no fue ingresado")

def Info_Estud():
    if Estudiantes:
        print("\n""Estudiantes ingresados y sus datos")
        for i, (nombre, datos) in enumerate(Estudiantes.items(), start=1):
            print(f"{i}. Estudiante: {nombre.capitalize()}  |  Edad: {datos['edad']}  |  Calificacion: {datos['calificacion']}")
    else:
        print("No has ingresado ningun estudiante")

def Elim_Estud():
    nombre = input("\n""Ingresa el nombre del estudiante que deseas eliminar: ").lower()
    if nombre in Estudiantes:
        del Estudiantes[nombre]
        print(f"Estudiante {nombre.capitalize()} a sido eliminado del sistema")
    else:
        print("Ese estudiante no fue ingresado")

def menu_estud():
    while True:
        print("\n""1. Agregar un nuevo estudiante")
        print("2. Modificar la calificacion de un estudiante")
        print("3. Mostar la informacion de todos los estudiantes")
        print("4. Eliminar un estudiante por su nombre")
        print("5. Salir del menu")

        opcion = int(input("\n""Ingresa la opcion que necesites (1-5): "))
        if opcion == 1:
            Agregar_Estud()
        elif opcion == 2:
            Mod_Estud()
        elif opcion == 3:
            Info_Estud()
        elif opcion == 4:
            Elim_Estud()
        elif opcion == 5:
            print("¡¡Hasta luego. Vuelve pronto!!")
            break
        else:
            print("¡¡Ingresa una opcion valida!!")

menu_estud()

