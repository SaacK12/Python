lista= ["Alice", "Apsaras", "Ganesha", "High Pixie", "Hydra", "Incubus", "Ippon-Datara", "Jack Frost", "Mara", "Matador", "Nahobino", "Nekomata", "Nuwa", "Rakshasa", "Shiva", "Succubus", "Tsuchigumo", "Yoshitsune", "Zhu Tun She"]
letra_buscar= input("Introduzca la letra con la que desea buscar: ")
letra_buscar= letra_buscar.upper()
contador_demonios= 0
for palabra in lista:
    if palabra[0] == letra_buscar:
        print(palabra)
        contador_demonios += 1
if contador_demonios >= 1:
    print(f"Hay {contador_demonios} demonio(s) que comienzan con esta letra.")
else:
    print("No se ha encontrado ningun demonio que comience con esta letra")