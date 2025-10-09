#######################################
#En este ejercicio me pinto por########
# ponerle verificaciones adicionales###
# aunque no lo pedian, igual reutilize#
#el codigo del trabajo grupal.#########
#######################################
def verificarNombres(nombre):
    while True:
        if nombre.isalpha(): #Esto verifica que el nombre sea solo letras
            return nombre
        else:
            nombre= input("Por favor, ingrese un nombre válido")

def verificarAño(nmr):
    while True:
            if nmr.isdigit() and len(nmr) == 4: #Esto verifica que sean numeros y de 4 digitoss
                return nmr
            else:
                nmr= input("Por favor, ingrese un número válido para la cantidad de curso.")

def diccionario(personas,**kwars):
    personas.append(kwars)

def calcular_edad(edad):
    edad_actual= año - edad
    return edad_actual

personas= []
vuelta= 1
año= input("Introduzca el año en curso: ")
año= int(verificarAño(año))
while vuelta <= 3:
    persona= input(f"Introduzca el nombre de la {vuelta}° persona")
    persona= verificarNombres(persona)
    persona_nacimiento= input(f"Introduzca el año de nacimiento de {persona}: ")
    persona_nacimiento= verificarAño(persona_nacimiento)
    diccionario(personas, nombre=persona, año= persona_nacimiento)
    vuelta= vuelta + 1

for persona in personas:
    edad_actual= int(persona['año'])
    edad_actual= calcular_edad(edad_actual)
    print(edad_actual)

#Dios mio como me arrepenti de ponerle validaciones al pedo,
#por eso me quedo tan largo y en como dos horas nomas hice este ejercicio.
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThXDY0GzYyH4_oVtjMYnzEUdvaz5THTHWqsw&s
#Bueno es una buena excusa para usar el teclado que me compre.