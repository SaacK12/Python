import tkinter as tk
from PIL import Image, ImageTk 
import random

def adivinar():
    comentario= caja_texto.get()
    if comentario == "":
        etiqueta_adivino.config(text= "No puedo responder a eso.")
    else:
        valor= random.randint(0,4)
        if valor == 0:
            etiqueta_adivino.config(text="Si")
        if valor == 1:
            etiqueta_adivino.config(text="No")
        if valor == 2:
            etiqueta_adivino.config(text="Definitivamente Si!")
        if valor == 3:
            etiqueta_adivino.config(text="Definitivamente No")
        if valor == 4:
            etiqueta_adivino.config(text="Tu que piensas?")

ventana= tk.Tk()
ventana.title("Psicho Mantis")
ventana.geometry("1000x1000")
ventana.resizable(0,0)


##Caja de Texto
caja_texto= tk.Entry(bg="#979797")
caja_texto.place(x=64, y=84, width=100, height=30)
##Boton 
boton= tk.Button(text="Enviar", bg="#DF7EF3", command= adivinar)
boton.place(x=90, y=150, width=100, height=25)
#etiqueta
etiqueta_adivino= tk.Label()
etiqueta_adivino.place(x=40, y=200)
#Imagen
imagen= Image.open("psycho-mantis.gif")
imagen_tk= ImageTk.PhotoImage(imagen)
labelImagen= tk.Label(ventana, image=imagen_tk)
redimensionado= imagen.resize((400,400))
redimensionado_tk=ImageTk.PhotoImage(redimensionado)
label= tk.Label(ventana, image=redimensionado_tk)
label.image= imagen_tk
label.pack()
ventana.mainloop()






##Mostrar la ventana
ventana.mainloop()