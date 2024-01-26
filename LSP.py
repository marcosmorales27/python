# class Ave:
#     def volar(self):
#         return "estoy volando"
    
# class Pinguino:
#     def volar(self):
#         return "no puede volar"
    
# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(delf):
        return "estoy volando"
    
class AveNoVoladora(Ave):
    pass