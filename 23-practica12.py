with open("tickets.txt", "r") as archivo:
    contenido = archivo.read()

lineas = contenido.split("\n")

tickets = []

for linea in lineas:
    datos = linea.split(",")

    ticket = {
        "ticket_id": datos[0],
        "vendor": datos[1],
        "mttr": datos[2]
    }

    tickets.append(ticket)

print(tickets)