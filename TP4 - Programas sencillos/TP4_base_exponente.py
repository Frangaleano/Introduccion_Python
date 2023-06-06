"""

Cree un script que lea dos números de teclado (una base y un exponente)
y luego muestre en pantalla el resultado de elevar el número base a la
potencia exponente.

"""

base = int(input("introduzca una base: "))
exponente = int(input("introduzca un exponente: "))
resultado = int(base**exponente)
print("el resultado es:", resultado)