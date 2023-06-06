"""

Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
uno, informarle si el mismo es positivo, negativo, o cero.

"""

for n in range(10):
   numero = int(input("Ingrese un numero: "))
   if numero > 0:
      print("el numero es positivo")
   elif numero < 0:
      print("El numero es negativo")
   else: 
      print("Elegiste el 0!") 



    
    


