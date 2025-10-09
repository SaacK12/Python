palabras= []
vueltas= 5
while vueltas != 0:
    palabra_introducida= input(f"Introduzca una palabra (palabras restantes: {vueltas}) ")
    palabras.append(palabra_introducida)
    vueltas -= 1

print(palabras[4])
print(palabras[3])
print(palabras[2])
print(palabras[1])
print(palabras[0])