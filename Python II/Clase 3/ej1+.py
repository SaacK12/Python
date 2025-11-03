personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
f= open("personas.txt", "w")
for nombre, edad in personas.items():
    linea= f"{nombre.lower()}-{edad}\n"
    f.write(linea)
    f.close