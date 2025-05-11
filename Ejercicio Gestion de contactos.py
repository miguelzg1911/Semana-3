# Ejercicio: Gestión de Contactos
# Objetivo:

# Crear un diccionario para gestionar los contactos, donde la clave sea el nombre del contacto y el valor sea su número de teléfono. 
# El programa permitirá agregar nuevos contactos.
# Instrucciones:

#     Crea un diccionario llamado contactos donde cada clave sea el nombre de un contacto y su valor sea el número de teléfono.

#     El programa debe permitir al usuario realizar las siguientes operaciones:
#         Agregar un nuevo contacto (nombre, número de teléfono).
#         Mostrar todos los contactos almacenados.
#         Buscar un contacto por su nombre.


contactos = {}

def agregar_cont():
    while True:
        nombre = input("\n""Ingresa el contacto: ")
        telefono = int(input("Ingresa el numero de telefono del contacto: "))
        contactos[nombre] = telefono
        print(f"Contacto que agregaste: {nombre} y su numero: {telefono}")
        new = input("\n""¿Deseas ingresar otro contacto? (si/no): ")
        if new == "si":
            continue
        else: 
            print("\n""__Vuelves al menu___")
            break

def mostrar_cont():
    print("\n""--Contactos que has ingresado--")
    if contactos:
        for i, (nombre, telefono) in enumerate(contactos.items()):
            print(f"{i+1}. Contacto: {nombre} | telefono: # {telefono}")
    else:
        print("No has ingresado ningun contacto")

def buscar_cont():
    buscar = input("\n""Ingresa el contacto que deseas buscar: ")
    if buscar in contactos:
        print(f"El contacto ({buscar}) si se encuentra agregado")
    else:
        print("No se ha encontrado el contacto")

while True:
    print("\n""---MENU---")
    print("1. Agregar un contacto nuevo")
    print("2. Mostrar todos los contactos almacenados")
    print("3. Buscar uncontacto por su nombre")
    print("4. Salir del menu")

    opcion = int(input("\n""Escoge la opcion que necesites (1-4): "))
    if opcion == 1:
        agregar_cont()
    elif opcion == 2:
        mostrar_cont()
    elif opcion == 3:
        buscar_cont()
    elif opcion == 4:
        print("---¡¡Vuelve pronto!!---")
        break
    else:
        print("Ingresa una opcion valida")

