def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(10, 5)

print(total)


def calcular_porcentaje_p1(total_tickets, tickets_p1):
    porcentaje = tickets_p1 / total_tickets * 100
    return porcentaje

resultado = calcular_porcentaje_p1(50, 15)

print(resultado)



def calcular_promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


mttr = [4.5, 7.2, 11.8, 3.9, 14.1]

resultado = calcular_promedio(mttr)

print(resultado)