from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod 
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"hola me llamo: {self.nombre} y tengo {self.edad} años")
        
class Mono(Animal):
    def __init__(self, nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"estoy: {self.actividad}")
        
class Condor(Animal):
    def __init__(self, nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f"estoy: {self.actividad}")
        
marcos = Mono("marcos",5,"masculino","saltando entre árboles")
joaquin = Condor("joaquin",10,"masculino","volando entre los Andes")

marcos.presentarse()
marcos.hacer_actividad()
joaquin.presentarse()
joaquin.hacer_actividad()