"""

Vuelva a construir el menú del ejercicio 6 del Trabajo Práctico VI, pero esta vez
agregue una nueva opción llamada “Salir”. El programa deberá mostrar el menú
y reaccionar a la opción seleccionada por el usuario, pero ahora, al ejecutar una
opción, en vez de terminar el programa, se mostrará nuevamente el menú,
hasta que el usuario seleccione la opción 4. Salir.

"""

import os

def menu():
    return print("1. Saludar\n2. Informar temperatura\n3. Mostrar nombre de la materia.\n4. Salir.")

def borrar():
    return os.system('cls')

entrada = True

while entrada:
    menu()
    entrada = int(input("Seleccione una opcion del menú principal: "))
    borrar()


    if entrada == 1:
        nombre = input("ingrese su nombre: ")
        print("Hola", nombre, "!")
        input("Ingrese ENTER para continuar...")
        borrar()

    elif entrada == 2:
        print("La temperatura es: 20 °C")
        input("Ingrese ENTER para continuar...")
        borrar()

    elif entrada == 3:
        print("La materia es introducción a la programación")
        input("Ingrese ENTER para continuar...")
        borrar()

    elif entrada == 4:
        print("Usted salio del programa, gracias.")
        entrada = False

    else:
        print("La opcion seleccionada NO esta dentro del menu\n")
        input("Ingrese ENTER para continuar...")
        borrar()
