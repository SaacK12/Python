extension= tuple(f".{i:00}" for i in range (100)) #.00, .01, 02, 03,
nombre= input("Introduzca el nombre del producto: ")
precio= input("Introduzca el precio del producto: ")
unidades= input("Introduzca la cantidad de unidades que va a comprar: ")
costeTotal= float(precio) * int(unidades)
if len(precio) < 6: #Esto comprueba que si el largo de "precio" es menor a 6 caracters, los rellenara con 0
    precio= precio.zfill(6)
if not precio.endswith(extension): #Esto comprueba que si "precio" no termina con alguna posibilidad de la tupla, lo añadira ".00"
    precio= precio + ".00"
if len(unidades) < 3: #Lo mismo que arriba
    unidades= unidades.zfill(3)
print("Precio: ",precio,"Unidades: ",unidades,"Coste Final: ",costeTotal)