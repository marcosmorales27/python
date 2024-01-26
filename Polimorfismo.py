class Gato():
    def sonido(self):
        return"miau"

class Perro():
    def sonido(self):
        return"woof"

def hacer_sonido(animal):
    print(animal.sonido())

#objetos    
gato = Gato()
perro = Perro()

#mismo mensaje
hacer_sonido(gato)

print(perro.sonido())