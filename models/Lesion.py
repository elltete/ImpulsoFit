class Lesion:
    
    def __init__(self, zona, grado, observaciones):
        self.__zona = zona
        self.__grado = grado
        self.__observaciones = observaciones

#Getters
    
    def get_zona(self):
        return self.__zona
    
    def get_grado(self):
        return self.__grado
    
    def get_observaciones(self):
        return self.__observaciones

