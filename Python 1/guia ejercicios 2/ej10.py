cesta= input("Introduzca los productos de la cesta separados por comas: ")
producto= []
producto= cesta.split(",")
for obj in producto:
    print(obj)