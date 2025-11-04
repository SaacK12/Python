import tkinter as tk
##Crear ventana##
ventana= tk.Tk()
ventana.title("CHECKBOXES EXAMPLE")
ventana.geometry("800x600")
ventana.resizable(0,0)
ventana.iconbitmap("C:\\Users\\Pc\\Documents\\Laburito\\Python\\Python II\\Clase 9 REPASAR\\sh2.ico")

## Crear checkboxes ##
lista=["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
var= [tk.IntVar() for i in range(len(lista))]
## ##

def mostrar_seleccion():
    seleccion= [lista[i] for i in range (len(lista)) if var[i].get() == 1]
    etiqueta.config(text=f"Seleccionaste: {', '.join(seleccion)}")
## Crear checkboxes ##
for i in range(len(lista)):
    check= tk.Checkbutton(ventana, text=lista[i], variable=var[i])
    check.pack()


boton= tk.Button(text="¡Presioname!",command=mostrar_seleccion)
boton.place(x=350, y=150, width=100, height=25)

etiqueta= tk.Label(bg="pink")
etiqueta.place(x=40, y= 100)
##Mantener ventana##
ventana.mainloop()
## ##