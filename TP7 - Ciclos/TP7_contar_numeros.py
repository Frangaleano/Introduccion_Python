"""

Cree un script para mostrar los primeros 100 números enteros positivos,
comenzando desde el 1.

"""


def contar_numeros(numero:int) -> int:
    for numero in range(numero,101):
        print(numero)

def main():
    resultado = 1
    contar_numeros(resultado)

main()
