lista= ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]
for n in lista:
    persona= n.split()
    nombre= persona[0]
    apellido= persona[1]
    print(f"{nombre.capitalize()} {apellido.capitalize()}")