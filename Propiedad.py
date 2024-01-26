class Persona:
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter    
    def nombre(self):
        del self.__nombre
    
marcos = Persona("Marcos", 58)

nombre = marcos.nombre
print(nombre)

marcos.nombre = "joaco"

nombre = marcos.nombre
print(nombre)

del marcos.nombre

print("que haces")