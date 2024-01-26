class TanqueDeCombustible:            
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible 
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("has movido el auto")
        else:
            print("no hay combustible")
            
    def obtener_posicion(self):
        return self.posicion
        
tanque = TanqueDeCombustible()
carro = Auto(tanque)

print(carro.obtener_posicion())
print(carro.mover(10))
print(carro.obtener_posicion())
print(carro.mover(20))
print(carro.obtener_posicion())
print(carro.mover(60))
print(carro.obtener_posicion())
print(carro.mover(100))
print(carro.obtener_posicion())
print(carro.mover(100))
print(carro.obtener_posicion())