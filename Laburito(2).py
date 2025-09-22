lista= [] #Esta es la lista principal que va a ir acumulando todos los diccionarios que carguemos.
def diccionario (lista, **kwargs):
    lista.append(kwargs) #Esta funcion agrega ese diccionario al final de la lista. (Sin pisarlo)
def buscar (nombre):
    encontrado= False
    for alumno in lista:
        if alumno["alumno"] == nombre:
            print("Los cursos de este alumno son:",alumno["curso"])
            encontrado = True
            break
    if not encontrado:
        print("El usuario introducido no se encontro")
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver lista de alumno")
    print("3 - Ver la cantidad de cursos de un alumno")
    print("4 - Salir.")
    numero = (input(">>"))
    if numero == "2":
        print("Lista de alumnos:")
        for alumno in lista:
            print(alumno["alumno"])
    if numero == "1":
        alumno= input("Ingrese el nombre del alumno: ")
        while True:
            if alumno.isalpha(): #Esto verifica que el nombre sea solo letras
                alumno= str(alumno)
                break
            else:
                print("Por favor, ingrese un nombre válido para el alumno.")
                alumno= input("Ingrese el nombre del alumno: ")
        curso= input("Ingrese la cantidad de curso: ")
        while True:
            if curso.isdigit(): #Esto verifica que el curso sea un numero entero
                curso = int(curso)
                diccionario(lista, alumno=alumno, curso=curso)
                print ("alumno añadido exitosamente! ")
                break
            else:
                print("Por favor, ingrese un número válido para la cantidad de curso.")
                curso= input("Ingrese la cantidad de curso: ")
    if numero == "3":
        nombre= input("Introduzca el nombre: ")
        buscar(nombre)
    if numero == "4":
        print("Gracias por usar nuestro programa.")
        break
    if numero != "1" and numero != "2" and numero != "3":
        print("Valor no valido")