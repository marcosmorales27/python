class Persona:
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
    
marcos = Persona("Marcos", 58)

nombre = marcos.get_nombre()
print(nombre)

marcos.set_nombre("juanceto01")
print(nombre)