import tkinter as tk
from PIL import Image, ImageTk  # Necesitarás instalar Pillow: pip install pillow

# Funciones para cambiar la imagen
def mostrar_imagen(index):
    img = Image.open(imagenes[index])
    img = img.resize((300, 200))
    img_tk = ImageTk.PhotoImage(img)
    etiqueta_imagen.config(image=img_tk)
    etiqueta_imagen.image = img_tk  # Para que no sea recolectada por el garbage collector

def siguiente():
    global imagen_index
    if imagen_index < len(imagenes) - 1:
        imagen_index += 1
    mostrar_imagen(imagen_index)

def anterior():
    global imagen_index
    if imagen_index > 0:
        imagen_index -= 1
    mostrar_imagen(imagen_index)

# Ventana principal
ventana = tk.Tk()
ventana.title("Galería de Imágenes")

# Lista de imágenes
imagenes = ["imagen1.png", "imagen2.jpg", "imagen3.jpg"]  # Sustituye con tus imágenes
imagen_index = 0

# Widget para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack()

# Botones para navegación
boton_anterior = tk.Button(ventana, text="Anterior", command=anterior)
boton_anterior.pack(side="left", padx=10)

boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente)
boton_siguiente.pack(side="right", padx=10)

# Mostrar la primera imagen
mostrar_imagen(imagen_index)

ventana.mainloop()