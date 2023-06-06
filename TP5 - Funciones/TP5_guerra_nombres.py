"""

Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
y retorne True si nombre1 tiene más letras que nombre2, o False en caso
contrario.

"""

def guerra_nombres(nombre1, nombre2):  


    resultado = bool(len(nombre1) > len(nombre2))
    
    return resultado

primer_nombre = input("coloque el primer nombre: ")
segundo_nombre = input("coloque el segundo nombre: ")

print("el resultado es: ", guerra_nombres(primer_nombre,segundo_nombre))