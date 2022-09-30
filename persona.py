class persona():
    #metodo contructor
    def __init__(self, numero,nombre,direccion):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion

    #getters
    def vernumero(self):
        return self.numero

    def vernombre(self):
        return self.nombre

    def verdireccion(self):
        return self.direccion 

    #setters
    def modificarnumero(self, nuevonumero):
        self.numero = nuevonumero
    
    def modificarnombre(self, nuevonombre):
        self.nombre = nuevonombre
   
    def modificardireccion(self, nuevadireccion):
        self.direccion = nuevadireccion    