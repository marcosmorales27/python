class Personajes ():
    def __init__(self, nombre, rol, ultimate):
        self.nombre = nombre + ", interesante"
        self.rol = "juega en " + rol
        self.ultimate = "su habilidad a nivel máximo es " + ultimate
    
personaje1 = Personajes("akshan","medio o por arriba","artimañas")
personaje2 = Personajes("volybear","jungla","tormenta incesante")

print(personaje1.nombre)
print(personaje1.rol)
print(personaje1.ultimate)
print(personaje2.nombre)
print(personaje2.rol)
print(personaje2.ultimate)