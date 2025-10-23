import sqlite3
conn= sqlite3.connect("productos.sqlite")

def verificar_numero(numero):
    while True:
        if numero.isdigit(): 
            return int(numero)
            break
        else:
            numero= input("Por favor, ingrese un numero valido.")

while True:
    print("Menu")
    print("1- Agregar productos.")
    print("2- Ver productos.")
    print("3- Salir.")
    opcion= input(">>> ")
    match opcion:
        case "1":
            id= input("Introduzca el ID del producto: ")
            id= verificar_numero(id)
            nombre= input("Introduzca el nombre del producto: ")
            precio= input("Introduzca el precio del producto: ")
            precio= verificar_numero(precio)
            conn.execute(
                "INSERT INTO productos (id, nombre, precio) VALUES (?, ?, ?)",
                (id, nombre, precio))
            conn.commit()
            print("Producto añadido con exito!")
        case "2":
            cursor= conn.cursor()
            cursor.execute("SELECT id, nombre, precio FROM productos")
            contenido_tabla= cursor.fetchall()
            print(contenido_tabla)
        case"3":
            conn.close()
            break