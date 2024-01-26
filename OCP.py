class Notificador:
    def __init__(self, ususario, mensaje):
        self.ususario = ususario
        self.mensaje = mensaje 
    
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
       print(f"enviando mensaje por mail a {self.usuario.email}") 
       
class NotificadorSMS(Notificador):
    def Notificar(self):
       print(f"enviando SMS a {self.usuario.sms}")
       
class NotificadorWhatsapp(Notificador):
    def Notificar(self):
       print(f"enviando whatsapp a {self.usuario.whatsapp}")
       
class NotificadorX(Notificador):
    def Notificar(self):
       print(f"enviando X a {self.usuario.x}")