vocales= ["a", "e", "i", "o", "u"]
def caracter(vcl):
    vcl= vcl.lower()
    if vcl in vocales:
        condicion= True
        print(condicion)
    else:
        condicion= False
        print(condicion)

vocal= input("Introduzca una vocal: ")
caracter(vocal)