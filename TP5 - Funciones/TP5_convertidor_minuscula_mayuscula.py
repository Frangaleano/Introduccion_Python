"""

Modifique la función del ejercicio anterior para que retorne dos versiones 
del string recibido como parámetro: primero la versión en minúsculas, y luego la
versión en mayúsculas.

"""


def convertidor_minuscula_mayuscula(palabra1):
    minuscula = str(palabra1)
    mayuscula = minuscula.upper()

    return minuscula,mayuscula

palabra = input("ingrese una palabra: ")
print("el resultado de la conversion es:", convertidor_minuscula_mayuscula(palabra))





