nombre= input("Introduzca su nombre: ")
while True:
    if nombre.isalpha:
        nombre= str(nombre)
        break
    else:
        nombre= input("Por favor ingrese un nombre valido: ")
letras= 0
for n in nombre:
    letras= letras + 1
print(nombre.upper(),"tiene",letras,"letras.")