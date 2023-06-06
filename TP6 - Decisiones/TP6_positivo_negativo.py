"""

Cree un script que le solicite al usuario ingresar un número por teclado, y le
informe con un mensaje si su número es positivo, negativo, o 0.

"""

def positivo_negativo(numero:int):
    if (numero > 0):
        print("Tu numero es positivo!")
    elif (numero < 0):
        print("Tu numero es negativo")
    else:
        print("Tu numero es 0")
    return positivo_negativo

numero_entrada = int(input("Igrese aqui su numero: "))


positivo_negativo(numero_entrada)

