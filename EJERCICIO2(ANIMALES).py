class Animal:
    def comer(self):
        print("el animal esta comiendo")
        
class Pez(Animal):
    def nadar(self):
        print("el animal esta nadando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando")
        
class Tiburon(Mamifero,Pez):
    pass

pez= Tiburon()

pez.comer()
pez.nadar()

print(Tiburon.mro())