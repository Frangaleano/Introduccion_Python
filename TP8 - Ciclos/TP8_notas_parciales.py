"""

Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
cargar. Una vez ingresadas las notas, el programa debe informar la nota
promedio (tenga cuidado de no incluir al -1 dentro del promedio).

"""

def entrada():
    return int(input("Ingresar notas para promediar (cuando ingrese -1 se detendra la cuenta): "))

ingresos = True
notas = []

while ingresos:
    ingresos = entrada()
    notas.append(ingresos)
    if ingresos == -1:
        notas.pop()
        print("ya no hay más notas para cargar.")
        resultado = sum(notas)
        dividendo = len(notas)
        print("El promedio de las notas es:" , (resultado/dividendo))
        #promedio = resultado / dividendo
        #print("El promedio de sus notas es:", promedio)
        ingresos = False