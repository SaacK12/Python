def vf(nombre):
     while True:
            if nombre.isalpha(): 
                nombre= str(nombre)
                break
            else:
                print("Por favor, ingrese un nombre de manera válida.")
                nombre= input("Ingrese el nombre : ")
                
def vfn(numero):
    while True:
            if numero.isdigit(): 
                return int(numero)
                break
            else:
                print("Por favor, ingrese un numero de manera valida.")
                numero= input("Ingrese un numero para el pedido: ")
    
#############################################################################################
nombre= input("ingrese el nombre del cliente: ")
vf(nombre)

combo1 = vfn(input("Ingrese cantidad de Combo 1: "))

combo2 = vfn(input("Ingrese cantidad de Combo 2: "))

combo3 = vfn(input("Ingrese cantidad de Combo 3: "))

postre = vfn(input("Ingrese cantidad de Postre: "))

PrecioCombo1 = 7

PrecioCombo2 = 3

PrecioCombo3 = 5

PrecioPostre = 4

totalCostoCombo1 = PrecioCombo1 * combo1

totalCostoCombo2 = PrecioCombo2 * combo2

totalCostoCombo3 = PrecioCombo3 * combo3

totalCostoPostre = PrecioPostre * postre


total= totalCostoCombo1 + totalCostoCombo2 + totalCostoCombo3 + totalCostoPostre

print("el precio total del pedido es de $" , total)

while True:
    
    paga= vfn(input("Abona con $"))
    if paga < total:
        print("¡¡¡ FALTA DINERO PARA COMPRAR EL PEDIDO !!!")
    else:
        break    
vuelto= paga - total

print("el vuelto para el cliente es de $" , vuelto)


while True:

    FinPedido=  input("¿Confirma pedido? Y/N : ").lower()
    match FinPedido:
        case "y":
            print(" ¡¡ Pedido Guardado !!") 
            
            break 
        case "n":
            print("¡¡ Pedido Eliminado !!")
            break
            
        case _:
            print("ERROR , Confirme el pedido con Y o no con N ")