palabra_uno= input("Introduzca la primera palabra: ")
palabra_dos= input("Introduzca la segunda palabra: ")
if palabra_uno[-3] == palabra_dos[-3]:
    print("Las ultimas tres palabras riman!")
elif palabra_uno[-2] == palabra_dos[-2]:
    print("Al menos riman un poco!")
else:
    print("No riman!")