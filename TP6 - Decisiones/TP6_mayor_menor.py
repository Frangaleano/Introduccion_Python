"""

Cree un script que le solicite al usuario ingresar un número por teclado, y
luego le informe en pantalla si su número es mayor que 10; antes de finalizar
e independientemente de lo que haya sucedido antes, el script mostrará un
mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

"""

def mayor_10(numero: int):
    if (numero > 10):
        print("Tu numero", numero, "es mayor que 10.")
    else: 
        print("Tu numero es menor que 10")
    print("Saludos!")

numero_entrada = int((input("Ingrese su numero: ")))

mayor_10(numero_entrada)
