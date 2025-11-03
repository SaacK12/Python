print("MENU DE OPCIONES")
print("[1] Ventas")
print("[2] Pagos")
print("[3] Servicio tecnico")
print("[4] Gerencia")
num = input(">>>")
match num:
    case 1:
        print("Elegiste Ventas")
    case 2:
        print("Elegiste Pagos")
    case 3:
        print("Elegiste Servicio tecnico")
    case 4:
        print("Elegiste gerencia")