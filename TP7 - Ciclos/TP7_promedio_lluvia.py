"""

Un cliente ha solicitado un programa que le permita ingresar los mililitros de
lluvia caídos diariamente en una semana, para que el programa le informe en
pantalla el promedio de precipitación de esa semana. El cliente también desea
saber cuál fue el día en que más llovió en la semana.

"""



def cuenta_lluvia(cuenta):
    total = cuenta / 7
    return round(total, 2)

def dias_mas_lluvia(lista: list):
    if max(lista) == lista[0]:
        print("El dia con mayor precipitacion fue el dia domingo")
    elif max(lista) == lista[1]:
        print("El dia con mayor precipitacion fue el dia lunes")
    elif max(lista) == lista[2]:
        print("El dia con mayor precipitacion fue el dia martes")
    elif max(lista) == lista[3]:
        print("El dia con mayor precipitacion fue el dia miercoles")
    elif max(lista) == lista[4]:
        print("El dia con mayor precipitacion fue el dia jueves")
    elif max(lista) == lista[5]:
        print("El dia con mayor precipitacion fue el dia viernes")
    else:
        print("El dia con mayor precipitacion fue el dia sabado")

def imprimir_promedio(total):
    print("El promedio de precipitaciones fue de:",
      total, "mls esta semana.")



dias = []
promedio = 0


for i in range(1, 8):
    ingreso = int(
        input("Ingrese los mililitros de lluvia caídos diariamente: "))
    promedio += ingreso
    resultado = cuenta_lluvia(promedio)
    dias.append(ingreso)

imprimir_promedio(resultado)
dias_mas_lluvia(dias)

