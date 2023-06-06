"""

Dada una lista de números enteros, escribir una función para cada uno de los
siguientes ítems:
a- Devuelva una lista con todos los números que sean primos.
b- Devuelva la sumatoria y el promedio de los valores.
c- Devuelva una lista con el factorial de cada uno de esos números.

"""

numeros_naturales = []
numeros_primos = []
entrada = True
while entrada:
    ingreso = int(input("ingrese numeros a la lista(si quiere terminar ingrese 0): "))
    if ((ingreso/2) == 0) and ((ingreso/3) == 0):
        numeros_naturales.append(ingreso)  
        entrada = True
        if (ingreso == 0):
            print("Usted salio del programa")
            print("numeros primos:", numeros_primos)
            print("numeros naturales:", numeros_naturales)
            entrada = False
    else:
        numeros_primos.append(ingreso)