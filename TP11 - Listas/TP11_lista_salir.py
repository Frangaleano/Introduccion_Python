"""

Diseñe una función que reciba una lista, vacía o no, e incorpore números hasta que
el usuario ingrese el valor “salir”. Cuando termina de ingresar los datos, la
función debe retornar la lista al programa principal.

"""

lista = []

def lista_salir(entrada):
    entrada = True
    while entrada:
        ingreso = input("ingrese lo que quiera agregar a la lista (ingrese 'salir' para terminar): " )
        lista.append(ingreso)
        if ingreso == "salir":
            print("Usted Salio del programa, chauuu!")
            lista.pop()
            print(lista)
            entrada = False
    return entrada

lista_salir(entrada = str)