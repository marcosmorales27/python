class Celular:
    #instanciar 
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo= modelo
        self.camara = camara 
        
    def llamar(self):
        print(f'estas llamando desde un: {self.modelo}')
        
    def colgar(self):
        print(f'estas colgando desde un:  {self.modelo}')
        
celular1 = Celular("samnsung","S5","48MP")
celular2 = Celular("iphone","X","48MP")
celular3 = Celular()
celular4 = Celular()

print(celular1.colgar())