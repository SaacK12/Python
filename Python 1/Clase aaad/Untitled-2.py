a= input("Ingrese el año")
a= int(a)
if (a % 400) == 0:
    print ("El año es bisiestro")
else:
    if (a % 4) == 0 and (a % 100) != 0:
        print ("El año es bisiestro")
    else:
        print ("El año no es bisiestro")