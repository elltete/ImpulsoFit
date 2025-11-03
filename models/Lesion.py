class Lesion:
    
    def __init__(self, tipo_lesion, zona, grado, gravedad, observaciones):
        self.__tipo_lesion = tipo_lesion
        self.__zona = zona
        self.__grado = grado
        self.__gravedad = gravedad
        self.__observaciones = observaciones

#Getters
    def get_tipo_lesion(self):
        return self.__tipo_lesion
    
    def get_zona(self):
        return self.__zona
    
    def get_grado(self):
        return self.__grado
    
    def get_gravedad(self):
        return self.__gravedad
    
    def get_observaciones(self):
        return self.__observaciones

