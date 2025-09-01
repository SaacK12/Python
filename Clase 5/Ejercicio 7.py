peso= (input("Introduzca su peso"))
peso= float(peso)
while peso < 1:
    peso= float(input("Por favor intruzca su peso en valores positivos"))
    peso= float(peso)
altura= (input("Introduzca su altura"))
altura= float(altura)
while altura < 1:
    altura= float(input("Por favor intruzca su altura en valores positivos"))
    altura= float(altura)
alturaM= altura * altura
imc= peso / alturaM
imc= round(imc,2)
print(imc)