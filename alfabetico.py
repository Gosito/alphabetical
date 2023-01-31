palabras = []
print("Ordenador de palabras de A a la Z")
ingresar = int(input("Número de palabras: "))
for x in range (0, ingresar):
    palabras.append(input("Ingresar: "))
print(sorted(palabras))
