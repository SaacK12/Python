frutas= ("manzana", "banana", "pera", "naranja")
fruta_solicitada= input("Introduzca la fruta que desea: ")
for f in frutas:
    encontrada= False
    if fruta_solicitada == f:
        print("La fruta", f,"se encuentra en la tupla!")
        encontrada= True
        break
if encontrada == False:
    print("No se ha encontrado la fruta en la tupla.")