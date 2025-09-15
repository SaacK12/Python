lista=[]
numeros= (input("Introduzca una serie de numeros separados por una coma"))
lista= (numeros.split(","))
resultado= 0
for i in lista:
    resultado= resultado + i
print(resultado)