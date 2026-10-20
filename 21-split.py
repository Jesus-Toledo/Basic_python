linea = "INC2001,IZZI,5.5"

datos = linea.split(",")

print(datos)
print(datos[0])
print(datos[1])
print(datos[2])

with open("tickets.txt", "r") as archivo:
    contenido = archivo.read()

lineas = contenido.split("\n")