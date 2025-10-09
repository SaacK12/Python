def rima(p1,p2):
    ultimasTresLetrasP1= p1[-3:]
    ultimasTresLetrasP2= p2[-3:]
    while True:
        if ultimasTresLetrasP1 == ultimasTresLetrasP2:
            print("Riman perfectamente!")
            break
        elif ultimasTresLetrasP1[-2:] == ultimasTresLetrasP2[-2:]:
            print("Bueno, riman un poco!")
            break
        else:
            print("Ambas palabras no riman en lo absoluto")
            break
palabraUno= input("Introduzca una palabra")
palabraDos= input("Introduzca otra palabra")
rima(palabraUno,palabraDos)
