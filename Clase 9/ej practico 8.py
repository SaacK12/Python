def superposicion(list1, list2):
    enComun= 0
    for a, b in zip(list1, list2):
        if a == b:
            enComun += 1
    if enComun > 0:
            print("Hay al menos", enComun,"caracters en comun.")
    else:
            print("No hay ningun caracter en comun.")

string= input("aaa1")
listaUno= string.split()
string2= input("aaa2")
listaDos= string2.split()
superposicion(listaUno, listaDos)