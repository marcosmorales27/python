class MiClase:
    def __init__(self):
        #un guion privado, dos guiones muy privado
        self.__atributo_privado = "2711"

    def _hablar(self):
        print("hola")

objeto = MiClase()
print(objeto._hablar)