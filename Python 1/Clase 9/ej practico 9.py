def generar_n_caracteres(stg):
    lista= stg.split()
    #print(lista) Only for debugging (Se hace el bilingüe el)
    caracter= lista[0]
    cantidad= int(lista[1])
    vueltas= 0
    while vueltas < cantidad:
        print(caracter)
        vueltas += 1

lista= input("Introduzca un caracter y un numero separado por un espacio: ")
generar_n_caracteres(lista)