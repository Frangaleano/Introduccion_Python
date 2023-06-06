"""

Cree un script que, al ejecutarlo, le solicite al usuario ingresar su nombre
de pila, luego lo salude y calcule la cantidad de letras del nombre,
mostrando el mensaje “Hola, [NOMBRE], tu nombre tiene [N] letras.”.

"""

nombre = input("¿Cual es tu nombre?: ")
letras = len(nombre)
print("Hola", nombre, "tu nombre tiene:", letras, "letras.")