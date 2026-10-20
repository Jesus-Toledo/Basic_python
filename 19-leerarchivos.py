archivo = open("tickets.txt", "r")

contenido = archivo.read()

print(contenido)

archivo.close()



with open("tickets.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)