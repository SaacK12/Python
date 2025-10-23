import tkinter as tk

def sumar():
    numero_1= int(caja1.get())
    numero_2= int(caja2.get())
    resultado.config(text= numero_1 + numero_2)
#Crear ventana
ventana= tk.Tk()
ventana.title("Calculadora")
ventana.config(width=800, height=600)

##Crear caja texto
caja1= tk.Entry()
caja1.place(x=64, y=84, width=30, height=30)
caja2= tk.Entry()
caja2.place(x=120, y=84, width=30, height=30)
#Boton
boton1= tk.Button(text="Calcular", command= sumar)
boton1.place(x=140,y=84, width=130, height=30)
#etiqueta
resultado= tk.Label(bg="gray")
resultado.place( x=120 ,y=120, width=130, height=30)
##Mostrar la ventana
ventana.mainloop()