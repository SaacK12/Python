while True:
    try:
        a= float(input("Introduzca el primer numero: "))
        b= float(input("Introduzca el segundo numero: "))
        break
    except ValueError:
        print("El valor que ha introducido no es un numero valido.")
suma= a + b
print(f"La suma de {a} + {b} es: {suma}")
resta= a + b
print(f"Su resta da como resultado: {resta}")
multiplicar= a * b
print(f"Su multiplicacion: {multiplicar}")
try:
    division= a / b
    print(f"Y su division da: {division}")
except ZeroDivisionError:
    print("La division no es posible de realizarla por que el segundo numero es un cero.")