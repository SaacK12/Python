import tkinter as tk
####
##Crear ventana##
ventana= tk.Tk()
ventana.title("Lista Tareas")
ventana.geometry("320x280")
ventana.resizable(0,0)
###
#Almacenara todos los checkbox crados en una lista, y sus respectivas variables en otra aparte
checkboxs= []
variables= []
def agregar_tarea():
    texto= caja_texto.get()
    if texto != "":
        ##crear nueva variable
        var= tk.IntVar()
        variables.append(var)
        ##Crear checkbox
        check = tk.Checkbutton(ventana, text=texto, variable=var)
        checkboxs.append(check)
        check.pack()
        ##
        caja_texto.delete(0, tk.END)

#Para borrar en un bucle se accedera a todos los checkboxs creados, 
# y si alguno de esos tiene un boleano en 1, 
# procedera a borrarlo de la lista y a destruirlo de la interfaz
def borrar():
    #Iteramos en reversa usando range(start, stop, step)
    for i in range(len(checkboxs)-1, -1, -1):
        if variables[i].get() == 1:
            checkboxs[i].destroy()
            checkboxs.pop(i)
            variables.pop(i)


caja_texto= tk.Entry(bg="#979797")
caja_texto.pack()

boton_añadir= tk.Button(text="Añadir", command=agregar_tarea)
boton_añadir.pack()

boton_borrar=tk.Button(text="Borar",bg="red", command=borrar)
boton_borrar.pack()
##Mantener ventana##
ventana.mainloop()
## ##