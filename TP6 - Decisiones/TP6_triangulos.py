"""

Cree un script que determine si un triángulo es isósceles, equilátero, o
escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
números, correspondientes a los tres lados del triángulo.
equilátero = todos los lados iguales
isósceles = dos lados iguales
escaleno = todos los lados diferentes

"""


def triangulos(lado1:int, lado2:int, lado3:int):
    if(lado1 == lado2 == lado3):
        print("Ya que los 3 lados son iguales el triangulo es Equilátero")
    elif(lado1 != lado2) and (lado2!= lado3) and (lado3 != lado1):
        print("Como los 3 lados son distintos el triangulo es Escaleno")
    else:
        print("Tenemos dos lados iguales, entonces el triangulo es Isósceles")
    return triangulos

lado1_entrada = int(input("Coloque aca el valor del primer lado: "))
lado2_entrada = int(input("Coloque aca el valor del segundo lado: "))
lado3_entrada = int(input("Coloque aca el valor del tercer lado: "))

triangulos(lado1_entrada, lado2_entrada, lado3_entrada)
