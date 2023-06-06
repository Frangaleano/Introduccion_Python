"""

Cree una función que reciba dos números como parámetro, y muestre en
pantalla la suma aritmética de ambos. Invoque a la función con dos números
leídos desde teclado.

"""

def suma_aritmetica_simple(numero1, numero2):
    """
    defino la funcion con el nombre y le asigno dos parametros, luego los sumo e imprimo el resultado
    """
    resultado = 0
    resultado = numero1 + numero2
    print("El resultado de la suma es: ", resultado)

primer_numero = int(input("Introduzca un numero: "))
segundo_numero = int(input("introduca otro numero: "))

suma_aritmetica_simple(primer_numero, segundo_numero)

