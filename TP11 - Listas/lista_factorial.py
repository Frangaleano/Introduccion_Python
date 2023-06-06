"""

Dada una lista de números enteros y un entero k, escribir una función para
cada uno de los siguientes ítems:
a- Devuelva tres listas, una con los menores, otra con los mayores y otra con los
iguales a k.
b- Devuelva una lista con aquellos que son múltiplos de k.


"""

valores = []
entrada = True

while entrada:
    ingreso = int(input("Ingrese numeros para factoriar(ingrese '0' para salir): "))
    for n in valores:
        resultado = ingreso * n 
        valores.append(resultado)
    if ingreso == 0:
        print("El factorial de cada numero es:",valores )
        entrada = False


