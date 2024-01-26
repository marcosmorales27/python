class Celular ():
    def __init__(self, marca, modelo, camara):
        self.marca = marca + " es good"
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'estas llamando desde un: {self.modelo}')
        
    def cortar(self):
        print(f'estas cortando la llamada desde un: {self.modelo}')
        
        
celular1 = Celular("iphone","X","48MP")
celular2 = Celular("samsung","S5","60MP")

celular1.cortar()
