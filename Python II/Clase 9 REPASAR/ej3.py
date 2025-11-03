import tkinter as tk

# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        variable = tk.IntVar()  # Variable para almacenar el estado de la checkbox
        variables.append(variable)
        nueva_tarea = tk.Checkbutton(ventana, text=tarea, variable=variable)
        nueva_tarea.pack(anchor="w")
        checkbuttons.append(nueva_tarea)
        entrada_tarea.delete(0, tk.END)

# Función para eliminar tareas completadas
def eliminar_completadas():
    for i in reversed(range(len(variables))):
        if variables[i].get() == 1:  # Si está marcado
            checkbuttons[i].pack_forget()  # Ocultar checkbox
            del checkbuttons[i]  # Eliminar de la lista
            del variables[i]  # Eliminar variable asociada

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Entrada de texto para nueva tarea
entrada_tarea = tk.Entry(ventana)
entrada_tarea.pack(pady=10)

# Botón para agregar tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Botón para eliminar tareas completadas
boton_eliminar = tk.Button(ventana, text="Eliminar Completadas", command=eliminar_completadas)
boton_eliminar.pack(pady=5)

# Listas para almacenar checkboxes y variables
checkbuttons = []
variables = []

ventana.mainloop()