palabra= "FOXHOUND"

def contar_vocales(plb):
    letra_a= 0
    letra_e= 0
    letra_i= 0
    letra_o= 0
    letra_u= 0
    plb= plb.lower()
    for letra in plb:
        if letra == "a":
            letra_a += 1
        elif letra == "e":
            letra_e += 1
        elif letra == "i":
            letra_i += 1
        elif letra == "o":
            letra_o += 1
        elif letra == "u":
            letra_u += 1
    print("Esta palabra tiene", letra_a, "letras A")
    print(letra_e, "letras E")
    print(letra_i, "letras I")
    print(letra_o, "letras O")
    print(letra_u, "letras U")
contar_vocales(palabra)