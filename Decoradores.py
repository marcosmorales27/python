def decorador(funcion):
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()
        print("despues de llamar la funcion")
    return funcion_modificada

# def saludo():
#     print("hola marcos como estas")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("hola persona como estas, soy un robot")
    
saludo()