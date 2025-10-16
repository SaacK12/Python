def vf(nombre):
    while True:
        if nombre.isalpha():
            nombre= str(nombre)
            break
        else:
            print("Por favor, ingrese un nombre de manera valida.")
            nombre= input("Ingresa el nombre: ")

def cambio_de_turno(nombre):
    nombre = input("ingrese Nombre Del encargado ")
    vf(nombre)

encargado = input("ingrese Nombre Del encargado ")
vf(encargado)
while True:
    print(f"Welcome back {encargado} To The Los Pollos Hermanos Family")
    print("1. Ingresa Nuevo pedido")
    print("2. Cambio de turno")
    print("3. Apagar Sistema")
    opcion = input(">>> ")
    match opcion:
        case "1":
            print("Wachin")
        case "2":
            encargado= cambio_de_turno(encargado)
            vf(encargado)
        case "3":
            print("¡¡Gracias por Trabajar en Los Pollos Hermanos!!")
            break
        case _:
            print("Opcion Invalida")