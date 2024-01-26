class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("estoy hablando")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"mi habilidad es: { self.habilidad}")
        
    class EmpleadoArtista(Persona,Artista):
        def __init__(self,  nombre, edad, nacionalidad, habilidad, salario, empresa):
            Persona.__init__(self, nombre, edad, nacionalidad)
            Artista.__init__(self, habilidad)
            self.salario = salario
            self.empresa = empresa   
        
        def mostrar_habilidad(self):
            print("no tengo")
            
        def presentarse(self):
            print f'hola soy: {self.nombre}, {self.mostrar_habilidad()}y trabajo en {self.empresa}'
            
            
    roberto = EmpleadoArtista("roberto", 45, "ecuatoriano","cantar","google", 1000)
    
    roberto.presentarse
    
    herencia = issubclass(EmpleadoArtista, Persona)
    instancia = isinstance(roberto, Artista)
    
    print(instancia)
    