"""

Cree un script que le solicite al usuario ingresar dos números por teclado, y
luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
de que los números sean iguales, y muestre un mensaje acorde.

"""

def numero_mayor(numero1:int, numero2:int):
    if(numero1 > numero2):
        print(numero1, "es mayor que", numero2)
    elif (numero2 > numero1):
        print(numero2, "es mayor que", numero1)
    else:
        print("Los dos numeros son iguales")
    return numero_mayor


primer_numero = int(input("Coloque aqui el primer numero: "))
segundo_numero = int(input("Ingrese aqui el segundo numero: "))

numero_mayor(primer_numero,segundo_numero)