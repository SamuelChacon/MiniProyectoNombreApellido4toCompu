class persona():
    #metodo contructor
    def __init__(self, numero,nombre,direccion):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion

    def vernumero(self):
        return self.numero

    def vernombre(self):
        return self.nombre

    def verdireccion(self):
        return self.direccion  
