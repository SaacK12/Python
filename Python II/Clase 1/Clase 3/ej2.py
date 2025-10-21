personas = {}

try:
    with open("personas.txt","r") as f:
        datos = f.readlines()
    for n in datos:
        p = (n.strip()).split("-")
        personas[p[0].capitalize()] = int(p[1])
    print("Rescatados")
    print(personas)
except FileNotFoundError:
    print("No se puede recuperar")
