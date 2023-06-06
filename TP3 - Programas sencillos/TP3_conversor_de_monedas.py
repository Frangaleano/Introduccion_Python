"""

Cree un script que, sabiendo cuántos pesos argentinos tiene una persona
ahorrada en su cuenta (almacenando ese monto en una variable), muestre
en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
$14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
formato:

"""


pesos_argentinos = int(input("introduzca cuantos pesos tiene: "))
valores = [80.5 , 14.1 , 69.5]
dolares , reales, euros = valores
print("Usted tiene:", round(pesos_argentinos / dolares, 2), "dolares,", 
round(pesos_argentinos / reales, 2), "reales, o", 
round(pesos_argentinos / euros, 2), "euros.")

##print("Usted tiene:", round(pesos_argentinos / reales, 2), "reales.")
##print("Usted tiene:", round(pesos_argentinos / euros, 2), "euros.")