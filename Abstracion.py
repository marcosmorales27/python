class Celular:
    def __init__(self):
        self._estado = "descargando"
        
    def encender(self):
        self._estado = "encendido"
        
    def descargando(self):
        if self._estado == "descargando":
            self.encender()
        print("el celular esta descargando apilaciones")
        
mi_celu = Celular()
mi_celu.descargando()  