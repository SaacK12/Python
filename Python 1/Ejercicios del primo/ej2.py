numeros= []
numero_uno= int(input("Introduce el primer numero"))
numeros.append(numero_uno)
numero_dos= int(input("Introduce el segundo numero"))
numeros.append(numero_dos)
numero_tres= int(input("Introduce el tercer numero"))
numeros.append(numero_tres)

mayor= 0
for n in numeros:
    if n > mayor:
        mayor = n

print(mayor)