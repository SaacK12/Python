personas= {} #Diccionario vacio. No lista. 

while True:
    print("Seleccione una opcion")
    print("1. Agregar")
    print("2. Mostrar el mas chico")
    print("3. Mostrar el mas grande.")
    print("4. Salir.")
    opcion= input(">>> ")
    if opcion == "1":
        nombre= input("Introduzca el nombre: ")
        edad= int(input("Introduzca la edad: "))
        personas[nombre] = edad #Agrega esa pareja clave-valor al diccionario. (Los nombres de las variables (nombre y edad) los elegís vos.)
        #Ejemplo: Si el usuario escribe "Pedro" y "18"
        #Se guarda como personas = {"Pedro": 18}
    if opcion == "2":
        nombre_min = min(personas, key=personas.get)
        #min() busca la clave con el valor más bajo.
        #personas.get le dice a min que compare por el valor (las edades).
        #Entonces devuelve el nombre de la persona más chica.
        #
        print("El mas chico es:", nombre_min, "con:", personas[nombre_min]) #Cuando Python ve personas[nombre_min]
    if opcion == "3":                                                       #reemplaza nombre_min por su contenido, eso devuelve la edad
        nombre_max = max(personas, key=personas.get)
        print("El mas grande es", nombre_max, "con:", personas[nombre_max])
    if opcion == "4":
        break