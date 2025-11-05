class Rutina:
    
    def __init__(self, nombre, fecha_generacion, nivel, vigente):        
        self.__nombre = nombre
        self.__fecha_generacion = fecha_generacion
        self.__nivel = nivel
        self.__vigente = vigente

#Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_fecha_generacion(self):
        return self.__fecha_generacion
    
    def get_nivel(self):
        return self.__nivel
    
    def get_vigente(self):
        return self.__vigente
    