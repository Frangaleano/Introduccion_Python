"""

Cree una función que reciba dos números como parámetro (base y exponente),
y retorne el resultado de elevar base a la potencia exponente.

"""

def potenciacion(valor1, valor2):
    resultado = 0
    resultado = valor1 ** valor2
    return resultado

base = int(input("Coloque la base: "))
exponente = int(input("Coloque el exponente: "))

print("El resultado es:", potenciacion(base, exponente))
