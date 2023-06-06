"""

Cree un script para calcular el resultado de sumar los números desde el 75 al
150.

"""

def suma_numeros(n1,n2):
    suma_total = 0
    inicio = min(n1,n2)
    final = max(n1,n2)
    for n in range(inicio, final+1):
        suma_total = suma_total + n
    return suma_total

entrada1 = int(input("ingrese un numero: "))
entrada2 = int(input("ingrese un numero: "))
print("la suma total es", suma_numeros(entrada1, entrada2))



        
        




















        



