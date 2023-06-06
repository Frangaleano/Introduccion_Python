def es_numero_perfecto(numero):
    suma = 0
    verdad = bool
    for i in range(1,numero):
        if numero % i == 0:
            suma += i
            if suma == numero:
                verdad = False
            else:
                verdad = True

    return verdad

numero = 8

print(es_numero_perfecto(numero))


