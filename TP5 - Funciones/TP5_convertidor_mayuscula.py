"""

Cree una función que reciba un string como parámetro, y retorne el mismo
string, pero con todas las letras convertidas a mayúsculas.

"""

def convertidor_mayuscula(palabra): 
    """
    declaro la funcion y le asigno un parametro, luego realizo el pedido para ingresar la palabra y le paso la funcion upper para cambiarlo a mayuscula, eso lo guardo en la variable conversion y lo retorno en esa funcion,
    luego creo una variable y le asigno la funcion, para que se ejecute y lo que pongamos ahi se guarde en la variable del programa, para despues asignarlo en los parametro de la funcion e invocarla para dar imprimir el resultado.
    """
    conversion = input("Ingrese la palabra a convertir: ").upper()
    return conversion

entrada = convertidor_mayuscula
print("El resultado de la conversion es:", convertidor_mayuscula(entrada))
