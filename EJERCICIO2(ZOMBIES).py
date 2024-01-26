class Zombie:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        
class ZombiePlayero (Zombie):
    def __init__(self, nombre, edad,actividad):
        super().__init__(nombre, edad)
        self.actividad = actividad
        
    def mmosrtar_actividad(self):
        print(f"grado: {self.actividad}")
        
zombie = ZombiePlayero("Jose","198 años","flotar")
zombie.mostrar_datos()
zombie.mmosrtar_actividad()