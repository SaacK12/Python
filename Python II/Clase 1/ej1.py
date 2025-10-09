class persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad= e
    
    def cumpleaños(self):
        self.edad += 1
        

p = persona(input("Ingrese nombre:"),int(input("ingrese edad: ")))
p.cumpleaños()

print(f"{p.nombre} cumple {p.edad} años hoy")