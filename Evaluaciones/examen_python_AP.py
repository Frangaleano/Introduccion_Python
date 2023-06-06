# escriba una funcion que toma una lista vacia y retorne el numero impar mas chico de la lista.

def minimo(lista):
    lista_impares = []
    for n in lista:
        if n % 2 > 0:
            lista_impares.append(n)
    minimo = min(lista_impares)
    return minimo

# promedio lista hasta -1

def calcula_promedio_w(lista):
    promedio,contador,sumatoria = 0,0,0
    bandera = True
    while bandera and contador!=len(lista):
        if(lista[contador]!=-1):
            sumatoria+=lista[contador] 
            contador+=1
        else:
            bandera=False
    promedio = round(sumatoria/contador,2)
    return promedio

#palindromo

def es_palindromo(cadena):
    """
    Esta función recibe una cadena de texto y devuelve True si es un palíndromo o False si no lo es.
    """
    verdad = bool
    # Eliminamos los espacios en blanco y convertimos la cadena a minúsculas
    cadena = cadena.lower().replace(" ", "")

    # Comparamos la cadena original con su versión invertida
    if cadena == cadena[::-1]:  
        verdad = True
    else:
        verdad = False
    return verdad

#divisores 

def contar_divisores(numero):
    suma = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            suma += i
    return suma
    
numero = 10

print(contar_divisores(numero))

















