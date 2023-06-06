"""

Cree una función que reciba un string como parámetro, y retorne la cantidad de
letras que posee. Luego, utilice la función para escribir un programa que solicite
ingresar el nombre del usuario, y luego muestre en pantalla cuántas letras tiene
ese nombre.

"""

def  contador_letras(palabra):
    letras = 0
    letras = len(palabra)
    return letras

nombre = input("Coloque aqui su nombre: ")
nombre2 = nombre

print(nombre2, "tiene:", contador_letras(nombre), "letras.")