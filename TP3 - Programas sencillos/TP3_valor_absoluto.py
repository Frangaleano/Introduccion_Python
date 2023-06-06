"""

Cree un script que almacene un número entero en una variable, y luego
muestre en pantalla su valor absoluto, con el mensaje “El valor absoluto de N
es |N|”. Finalmente, verifique que su programa funciona correctamente,
ejecutándolo con el valor 10 en la variable (la salida debería ser 10), y luego
con el valor -10 (la salida debería ser 10 nuevamente).

"""

numero = int(input("introduzca un numero: "))
valor = abs(numero)
print("el valor absoluto de", numero, "es:", valor)