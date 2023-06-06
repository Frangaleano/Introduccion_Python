"""

Cree un script que, dado un número de día de la semana ingresado por
teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
números y días de la semana es la siguiente:

"""

def dias_semanales(numero: int):
    if (numero == 1):
        print("Domingo")
    elif (numero == 2):
        print("Lunes")
    elif (numero == 3):
        print("Martes")
    elif (numero == 4):
        print("Miercoles")
    elif (numero == 5):
        print("Jueves")
    elif (numero == 6):
        print("Viernes")
    elif (numero == 7):
        print("Sabado")
    else:
        print("Su numero esta fuera del rango :(")
    return dias_semanales


numero_entrada = int(input("Ingrese un numero del 1 al 7: "))

dias_semanales(numero_entrada)
