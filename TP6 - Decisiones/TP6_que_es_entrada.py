"""

Python ofrece algunas funciones built-in para facilitar la implementación de
validaciones. A continuación se listan algunas de las más comunes:
valor.isdigit()
Retorna True si todos los caracteres de valor son numéricos, False en caso
contrario.
valor.isalpha()
Retorna True si todos los caracteres de valor son alfabéticos (no
numéricos), False en caso contrario.
valor.isalnum()
Retorna True si valor es una combinación alfanumérica (caracteres y
números), False en caso contrario.
Codifique una función que reciba un parámetro cualquiera proveniente del
usuario del programa (que puede contener letras, números, o una combinación
de ambas), e indique si el mismo es un número, una palabra, o un valor
alfanumérico. Compruebe que su función resuelve el problema enviándole
valores correspondientes a las tres posibilidades.

"""



def que_es(texto:str) -> str:
    """defino la funcion y le asigno un parametro, luego utilizo ese parametro con las funciones y las guardo en variables locales, luego armo la estructura de condicionales para que el programa imprima el resultado segun el parametro ingresado
    """
    texto_numerico = texto.isdigit()   
    texto_caracteres = texto.isalpha()
    
    if (texto_numerico == True):
        print("Su texto son todos numeros")
    elif (texto_caracteres == True):
        print("Su texto son todos caracteres")
    else:
        print("Su texto son numeros y letras")
    
   
entrada = str(input("Coloque aqui su texto: "))

que_es(entrada)
    
