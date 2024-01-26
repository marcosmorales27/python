# class Diccionario:
#     def verificar_palabras(self, palabra):
#         #logica para verificar palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         pass

from abc import ABC, abstractmethod

class RastreadorDeNúmeros(ABC):
    @abstractmethod
    def verificar_numero(self, numeros):
        pass
    
class Guia(RastreadorDeNúmeros):
    def verificar_numero(self, numeros):
        pass
    
class ObtenerInformacion:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def obtencion_numeros(self, numero):
        
        obtenedor = RastreadorDeNúmeros(Guia)