lista= []
numero = int(input("Ingrese un rango"))
for i in range (3, numero+1,1):
    if i % 3== 0:
        lista.append(i)
for i in range (5, numero+1,1):
    if i % 5== 0:
        lista.append(i)    
print("Los multiplos de 3 y 5 son: ")    
print(lista)