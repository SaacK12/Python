import tkinter as tk

# Función para mostrar la opción seleccionada
def mostrar_opcion():
    opcion_seleccionada = f"Seleccionaste: {opcion.get()}"
    etiqueta_resultado.config(text=opcion_seleccionada)

# Ventana principal
ventana = tk.Tk()
ventana.title("Selecciona una opción")

# Variable para almacenar la opción seleccionada
opcion = tk.StringVar(value="Opción 1")

# Lista de opciones con Radiobuttons
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
for op in opciones:
    rb = tk.Radiobutton(ventana, text=op, value=op, variable=opcion)
    rb.pack(anchor="w")

# Botón para mostrar selección
boton = tk.Button(ventana, text="Mostrar Opción", command=mostrar_opcion)
boton.pack(pady=10)

# Etiqueta para mostrar la opción seleccionada
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()