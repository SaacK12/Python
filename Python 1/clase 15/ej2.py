lista= ["persona", "shin megami tensei", "Son of Liberty", "The Phantom Pain"]
def mas_larga(lis):
    palabra_mas_larga= ""
    for palabra in lis:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga= palabra
    print(palabra_mas_larga)
mas_larga(lista)