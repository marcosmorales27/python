class Libros:
    def __init__(self, nombre, genero, volumen):
        self.nombre = nombre
        self.genero = genero
        self.volumen = volumen
        
nombre = input("cual es su nombre: ")
edad = input("a que genero pertenece: ")
curso = input("de cual volumen buscas: ")

libro = Libros(nombre, genero, volumen)

print(f"""
      
      DATOS DEL LIBRO: \n\n
      nombre: {libro.nombre} \n
      edad:{libro.genero} \n
      curso:{libro.volumen} \n
      
      """)

while True:
    leer=input()
    if(leer.lower() == "leer"):
        libro.leer()