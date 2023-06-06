"""

Cree un script que le solicite a un alumno de la asignatura Introducción a la
Programación que ingrese las notas de sus dos parciales. Como resultado, se
le debe informar al alumno su situación, junto con la nota promedio. Las
reglas para saber la situación de un alumno son las siguientes:

"""

def notas_promedio(nota1:int, nota2:int):
    resultado = 0
    resultado = round((nota1 + nota2) / 2)
    if (resultado >= 8):
        print("Promovido! tu nota es", resultado)
    elif (resultado >= 4):
        print("Regular! debe rendir final. Tu nota es:", resultado)
    else: 
        print("Libre! podes recursar o rendir un final extendido. Tu nota es:", resultado)
    return notas_promedio


nota1_entrada = int(input("Coloque aca la primer nota: "))
nota2_entrada = int(input("Coloque aca la segunda nota: "))

notas_promedio(nota1_entrada, nota2_entrada)