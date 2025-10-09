entero= 14
lista= ["Ghost Babel", "Son of Liberty", "Snake Eater", "Portable Ops", "Guns of the Patriots", "Peace Walker", "Ground Zeros","The Phantom Pain"]
def  filtrar_palabras(lis):
    lista_palabras_filtradas= []
    for palabra in lis:
        if len(palabra) >= entero:
            lista_palabras_filtradas.append(palabra)
    print (lista_palabras_filtradas)

filtrar_palabras(lista)