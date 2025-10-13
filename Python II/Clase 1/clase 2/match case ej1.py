try:
    mes= (int(input("Ingrese un mes (Del 1 al 12): ")))
    match mes:
        case 1:
            print("Enero")
        case 2:
            print("Febrero")
        case 3:
            print("Marzo")
        case 4:
            print("Abril")
        case 5:
            print("Mayo")
        case 6:
            print("Junio")
        case 7:
            print("Julio")
        case 8:
            print("Agosto")
        case 9:
            print("Septiembre")
        case 10:
            print("Octubre")
        case 11:
            print("Noviembre")
        case 12:
            print("Diciembre")
        case _:
            print("El numero introducido no es valido")
except ValueError:
    print("El valor introducido no es un numero")