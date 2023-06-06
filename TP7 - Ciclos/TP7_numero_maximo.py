"""

Cree un script que le solicite al usuario ingresar 10 números, y una vez
ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.
Extienda el script del ejercicio anterior para que también informe el número
mínimo ingresado, y su posición.

Cree un script que le solicite al usuario ingresar 10 números, y una vez
ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

"""


valores = []

for i in range(1, 11):
        numeros = int(input("ingrese un numero (van a ser 10): "))
        valores.append(numeros)
        resultado = max(valores)
        resultado_minimo = min(valores)
        posicion_resultado = valores.index(resultado_minimo)
        
print("el numero maximo es:", resultado, "y el numero minimo es:", resultado_minimo, "que esta en la posicion numero:", posicion_resultado+1)
