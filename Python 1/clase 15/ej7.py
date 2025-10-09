tupla= ()
def verificarEdad(nmr1):
    while True:
            if nmr1.isdigit(): #Esto verifica que la edad sea un numero entero
                return nmr1
            else:
                nmr1= input("Por favor, ingrese un número válido para la edad: ")
vuelta= 1
while vuelta <= 10:
    nmr= input(f"Introduzca la edad de la persona{vuelta}°: ")
    nmr= int(verificarEdad(nmr))
    tupla= tupla + (nmr,) #Fun fact: lo que hace no es “añadir datos a la tupla”, sino crear una nueva tupla en cada iteración y reasignarla a la variable.
    vuelta= vuelta+1
mayores_20= 0
for edad in tupla:
    if edad >= 20:
        mayores_20= mayores_20 + 1
print(f"La cantidad de personas mayores de 20 es de: {mayores_20}")