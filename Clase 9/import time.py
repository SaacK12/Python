import random
import time
time.sleep(4)
print("Dado")
print("1= Tirar dado")
print("2= Salir")
opcion=input(">>>")
while True:
    if opcion == "1":
        print(random.randint(1,6))
        opcion=input(">>>")
    if opcion == "2":
        break
    else:
        print("Opcion no valida")