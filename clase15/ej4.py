cadena=  input("Introduzca una cadena de texto: ")
letras_mayusculas= 0
for l in cadena:
    if l.isupper():
        letras_mayusculas = letras_mayusculas + 1

print("La cadena introducida contiene",letras_mayusculas,"letras en mayuscula.")