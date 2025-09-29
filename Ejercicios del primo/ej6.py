numeros= []
total= 0
while True:
    numero_introducido= float(input("Ingrese un numero: "))
    if numero_introducido == 0:
        break
    else:
        numeros.append(numero_introducido)
for n in numeros:
    total = total + n 
print(total)