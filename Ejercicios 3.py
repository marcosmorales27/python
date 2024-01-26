class Personaje:
    def __init__ (self, nombre, poder, resistencia):
        self.nombre = nombre
        self.poder = poder
        self.resistencia = resistencia
        
    def __repr__ (self):
        return f"{self.nombre}(Poder: {self.poder}, Resistencia: {self.resistencia})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nuevo_poder = round(((self.poder + otro_pj.poder)/2)**1.5)
        nueva_resistencia = round(((self.resistencia + otro_pj.resistencia)/2)**1.5)
        return Personaje(nuevo_nombre, nuevo_poder, nueva_resistencia)
    
gatsu= Personaje("gatsu", 100, 100)
griffith = Personaje("griffith",100,100)
casca = Personaje ("casca", 130,140)

grifitsu = gatsu + griffith
grificas = grifitsu + casca

print(grificas)
print(grifitsu)
print(gatsu)
print(griffith)
print(casca)