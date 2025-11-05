class Equipamiento:
    
    def __init__(self, tipo, descripcion):
        self.__tipo = tipo
        self.__descripcion = descripcion

#Getters
    def get_tipo(self):
        return self.__tipo

    def get_descripcion(self):
        return self.__descripcion
