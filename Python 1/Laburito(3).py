lista= [] #Esta es la lista principal que va a ir acumulando todos los diccionarios que carguemos.
def diccionario (lista, **kwargs):
    lista.append(kwargs) #Esta funcion agrega ese diccionario al final de la lista. (Sin pisarlo)
def buscar (nombre):
    encontrado= False
    cantidadAlumnos= 0
    for alumno in lista:
        if alumno["alumno"] == nombre:
            print("Los cursos de este alumno son:",alumno["curso"])
            encontrado = True
            cantidadAlumnos= cantidadAlumnos + 1
    if cantidadAlumnos > 0:
        print("Se ha encontrado", cantidadAlumnos, "alumnos con este nombre")
    elif not encontrado:
        print("El usuario introducido no se encontro")

####Verificar Nombres#####

def verificarNombres(nombre):
    while True:
        if nombre.isalpha(): #Esto verifica que el nombre sea solo letras
            return nombre
        else:
            print("Por favor, ingrese un nombre válido para el alumno.")
            nombre= input("Ingrese el nombre del alumno: ")

#### Verificar Curso ####

def verificarCurso(nmr):
    while True:
            if nmr.isdigit(): #Esto verifica que el curso sea un numero entero
                return nmr
            else:
                print("Por favor, ingrese un número válido para la cantidad de curso.")
                nmr= input("Ingrese la cantidad de curso: ")

###### Menu #########

while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver lista de alumno")
    print("3 - Ver la cantidad de cursos de un alumno")
    print("4 - Salir.")
    numero = (input(">>"))
    
    ###### Lista de alumno #########
    
    if numero == "2":
        print("Lista de alumnos:")
        for alumno in lista:
            print(alumno["alumno"])
            
    ###### Añadir un alumno #########
    
    if numero == "1":
        alumno= input("Ingrese el nombre del alumno: ")
        alumno= verificarNombres(alumno) #retorna el valor valido
        alumno= str(alumno)
        curso= input("Ingrese la cantidad de curso: ")
        curso= verificarCurso(curso)
        curso = int(curso)
        diccionario(lista, alumno=alumno, curso=curso)
        print ("alumno añadido exitosamente!")
        
    ####### Ver cantidad de curso #########
    
    if numero == "3": 
        nombre= input("Introduzca el nombre: ")
        nombre= verificarNombres(nombre)
        buscar(nombre)
        
    ###### Salir ######
    
    if numero == "4":
        print("Gracias por usar nuestro programa.")
        break
    
    ##### Valores no validos del menu ######
    
    if numero != "1" and numero != "2" and numero != "3":
        print("Valor no valido")