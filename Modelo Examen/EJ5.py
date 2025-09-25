lista= ["FOX", "FOXHOUND", "OUTER HEAVEN", "PEACE WALKER", "THE PHANTOM PAIN", "EL PES 6666666666666666666"]

def mas_larga(lt):
    palabra_larga= ""
    for palabra in lt:
        if len(palabra) > len(palabra_larga):
            palabra_larga= palabra
    return palabra_larga
print(mas_larga(lista))
