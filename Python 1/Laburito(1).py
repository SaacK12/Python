lista= []
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")
    numero = (input(">>"))
    if numero == "1":
        print("Lista de alumnos:")
        print(lista)
    if numero == "2":
        alumno= input("Ingrese el nombre del pibe: ")
        curso= input("Ingrese la cantidad de curso: ")
        while True:
            if curso.isdigit(): #Esto verifica que el curso sea un numero entero
                curso = int(curso)
                break
            else:
                print("Por favor, ingrese un número válido para la cantidad de curso.")
                curso= input("Ingrese la cantidad de curso: ")
        lista.append(alumno + " - " + str(curso) + " cursos")
        print ("alumno añadido exitosamente! ")
    if numero == "3":
        print("Gracias por usar nuestro programa.")
        break
    if numero != "1" and numero != "2" and numero != "3":
        print("Valor no valido")