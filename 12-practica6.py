
tickets_dia = [20, 35, 28, 42, 25]

def calcular_promedio (tickets_dia):
    promedio_tickets = sum(tickets_dia) / len(tickets_dia)
    return promedio_tickets

resultado = calcular_promedio(tickets_dia)

print(resultado)
