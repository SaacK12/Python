lista= []
numero= int(input("Ingrese un numero: "))
numero= numero-1
while True:
        nombre= input("Ingrese un nombre: ")
        lista.append(nombre)
        if numero < len(lista):
            break
print("Los nombres de la lista son:")
for i in lista:
    print(i)

dato= (input("Ingrese un nombre de la lista: "))
cantidad= 0
for n in lista:
        if n == dato:
            cantidad= cantidad + 1
print(dato, "aparece",cantidad,"veces")