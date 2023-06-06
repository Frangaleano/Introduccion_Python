"""

Cree un script que lea dos números enteros por teclado, y luego muestre
en pantalla el resultado de la suma entre ellos.

"""

def suma_aritmetica(numero1,numero2):
    """
    declaro la funcion suma_aritmetica con los parametros numero1 y numero2, que luego se sumaran.
    """
    resultado = 0
    resultado = numero1 + numero2
    return resultado

a = int(input("introduzca un numero: "))
b = int(input("introduzca otro numero: "))

print("el resultado de la suma es:", suma_aritmetica(a,b))

