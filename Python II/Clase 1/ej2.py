class persona:
    def __init__(self, nomb, apell):
        self.nombre = nomb
        self.apellido = apell
        
    def nombre_completo(self):
        print(self.nombre +""+self.apellido)
        
class estudiante(persona):
    def __init__(self, nomb, apell, carr):
        super().__init__(nomb, apell)
        self.carrera = carr
        
    def mostrar_carrera(self):
        print (self.carrera)
        
x = estudiante(input("Ingrese un nombre: "), (input("Ingrese apellido: ")), (input("Ingrese la carrera: ")))
print(x.nombre)
print(x.apellido)
print(x.carrera)