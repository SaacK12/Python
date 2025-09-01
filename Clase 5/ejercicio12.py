pan= 3.49
descuento= 60
barrasVendidas= int(input("¿Cuantas barras de pan (Que no son del día.) han sido vendidas? "))
print("Precio de una barra de pan al dia:", pan)
print("Descuento por no ser pan fresco:",(descuento),"%")
resultado= (pan * barrasVendidas) * (1 - descuento / 100)
print("Coste final de barras de pan (Que no son del día) vendidas:",round(resultado, 2))