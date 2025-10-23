import tkinter as tk
def saludar():
    nombre= caja1.get()
    #print("Sion sos", nombre)
    etiqueta_saludo.config(text="Hola "+ nombre)

##Crear ventana
ventana= tk.Tk()
ventana.title("Bunzi Boddy")
ventana.config(width=800, height=600)
##Crear boton
boton1= tk.Button(text="Bottom Blue", bg="#3C85FA",command=saludar)
boton1.place(x=90, y=150, width=100, height=25)
##Crear caja texto
caja1= tk.Entry()
caja1.place(x=64, y=84, width=100, height=30)
##Crear etiqueta
etiqueta1= tk.Label(text="Nombre",bg="#3C85FA")
etiqueta1.place(x=40, y=20)
##Etiqueta 2
etiqueta_saludo= tk.Label()
etiqueta_saludo.place(x=40, y=200)
##Mostrar la ventana
ventana.mainloop()