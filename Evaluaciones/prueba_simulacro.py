def cuadrados(n1,n2): #No cambiar este encabezado
    resultado = []
    if n1 > n2 :
        hasta = n1
        desde = n2
    else:
        hasta = n2
        desde = n1
    for n in range(desde,hasta+1):
        n *= n
        resultado.append(n)
    return resultado

lista = [8,3,12,23,20,11,20,10,20,10,20]
print(cuadrados(10,6))