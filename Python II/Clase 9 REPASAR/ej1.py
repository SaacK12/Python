import tkinter as tk

def verificar():
    seleccion= [opciones[i] for i in range (len(opciones)) if variables[i].get() == 1]
    etiqueta_seleccion.config(text=f"seleccionaste: {','.join(seleccion)}")

ventana= tk.Tk()
ventana.title("Selección de checkboxes")
ventana.geometry("1000x1000")
ventana.resizable(0,0)
## checkbox
opciones= ["Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4"]
variables= [tk.IntVar() for v in opciones] #creara cada variable para guardar el estado dle checkbox

## Crear checkbuttons 
for i in range (len(opciones)):
    casilla= tk.Checkbutton(ventana, text=opciones[i], variable=variables[i])
    casilla.pack(anchor="w")


boton= tk.Button(ventana, text="Mostrar resultado",command= verificar)
boton.pack()

#etiqueta
etiqueta_seleccion= tk.Label(ventana, text="")
etiqueta_seleccion.pack()

##Mostrar la ventana
ventana.mainloop()