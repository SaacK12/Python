def verificar_nombre(nombre):
    while True:
        if nombre.isalpha():
            nombre= str(nombre)
            return nombre
            break
        else:
            print("Por favor, ingrese un nombre de manera valida.")
            nombre= input("Ingresa el nombre: ")

def cambio_de_turno(empleado):
    empleado = input("ingrese Nombre Del encargado ")
    return empleado

encargado = input("ingrese Nombre Del encargado ")
encargado= verificar_nombre(encargado)
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
            encargado= verificar_nombre(encargado)
        case "3":
            print("¡¡Gracias por Trabajar en Los Pollos Hermanos!!")
            break
        case _:
            print("Opcion Invalida")