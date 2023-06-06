"""

Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
usuario ingrese la palabra “parar”. A medida que se van ingresando las palabras,
el programa simplemente debe mostrarlas en pantalla. Al detectar la palabra
para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.

"""

palabra = True
while palabra:
    ingreso = input("Ingresar una palabra (o 'parar' para finalizar): ")
    print(ingreso)
    if ingreso == "parar":
        print("--TERMINADO--")
        palabra = False
