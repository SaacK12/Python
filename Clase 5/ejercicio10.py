payasoPeso= 112
munecaPeso= 75
payasosVendidos= int(input("¿Cuantos payasos han sido vendidos en el ultimo pedido? "))
munecasVendidos= int(input("¿Cuantas muñecas han sido vendidas en el ultimo pedido? "))
pesoTotal= (payasoPeso * payasosVendidos) + (munecaPeso * munecasVendidos)
print("El peso total del paquete que será enviado es de", pesoTotal,"gr.")
