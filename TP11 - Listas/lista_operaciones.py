def promedio_total():
    entrada = True
    valores = []
    divisor = 0
    while entrada:
        ingreso = int(input(
            "Ingrese numeros enteros para mostrar el total y el promedio. (ingrese '0' para finalizar): "))
        valores.append(ingreso)
        suma = sum(valores)
        divisor += 1
        if ingreso == 0:
            divisor -= 1
            print("Usted ah salido del programa!")
            print("El total es:", suma)
            print("El promedio es:", round(suma/divisor))
            entrada = False
    return promedio_total

promedio_total()
