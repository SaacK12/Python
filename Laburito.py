diccionario= {}
while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver lista de alumno")
    print("3 - Ver cantidad de cursos de alumno" )
    print("4 - Salir.")
    numero = (input(">>"))
    if numero == "2":
        print("Lista de alumnos:")
        print(diccionario)
    if numero == "1":
        alumno= input("Ingrese el nombre del pibe: ")
        while True:
            if alumno not in diccionario:
                    diccionario[alumno] = []
                    break
            else:
                print("Por favor, ingrese un nombre válido para el alumno.")
                alumno= input("Ingrese el nombre del pibe: ")
        curso= input("Ingrese la cantidad de curso: ")
        while True:
            if curso.isdigit():  # Verifica que el curso sea un número entero
                diccionario[alumno].append(int(curso))  # Añadimos el curso al alumno (puedes tener varios cursos por alumno)
                print(f"¡Alumno {alumno} añadido exitosamente con {curso} curso(s)! ")
                break
            else:
                print("Por favor, ingrese un número válido para la cantidad de curso.")
                curso= input("Ingrese la cantidad de curso: ")
    if numero == "4":
        print("Gracias por usar nuestro programa.")
        break
    if numero == "3":
        print(diccionario[alumno])
    if numero != "1" and numero != "2" and numero != "3":
        print("Valor no valido")