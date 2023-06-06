"""

Las estructuras alternativas pueden utilizarse para validar datos. Por
ejemplo, si se intenta crear una función que tome dos enteros como
parámetro y muestre el resultado de su división, puede ocurrir un error si el
denominador es cero. Utilice la estructura alternativa para validar que el
denominador no sea cero; en caso de serlo, la función deberá mostrar el
mensaje No se puede dividir por 0!” en lugar de intentar mostrar el
resultado.

"""

def mensaje_cero(numerador:int, denominador:int):
    resultado = 0
    if(denominador != 0 ):
        resultado = numerador / denominador
        print("Tu resultado es:", resultado)
    else:
        print("No se puede dividir por 0!")
    

numerador_entrada = int(input("Ingrese el numero que quiere numerador: "))
denominador_entrada = int(input("Coloque aqui el denominador: "))

mensaje_cero(numerador_entrada, denominador_entrada)
