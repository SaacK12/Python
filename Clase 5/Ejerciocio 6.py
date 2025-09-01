n=int(input("Introduzca un numero entero"))
while n < 1:
    n=int(input("Por favor, introduzca un numero entero"))
numeroUno= n * (n + 1)
resultado= numeroUno / 2
print("La suma de todos los enteros desde 1 hasta", n,"es:", resultado)