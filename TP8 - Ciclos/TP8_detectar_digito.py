"""

Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
programa debe ser capaz de solicitarle al usuario que reingrese el número
cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
vez que detecte un error de validación, informele al usuario cuál fue el error, con
los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

"""

ingreso = True

while ingreso:
    entrada = input("ingrese un numero entero entre 1 y 100: ")
    print("el numero ingresado fue:", entrada)
    if (entrada.isdigit()):
        numero = int(entrada)
        if (numero > 0 and numero < 100):
            print(numero, "es valido!, gracias")
            ingreso = False
        else:
            print("El numero esta fuera del rango!")
    else :
        print("el dato ingresado no es un numero")
    
    
    

        
    


