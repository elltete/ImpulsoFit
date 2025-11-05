class Ejercicio:
    
    def __init__(self, nombre, descripcion, zona_principal, nivel_sugerido, tipo):        
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__zona_principal = zona_principal
        self.__nivel_sugerido = nivel_sugerido
        self.__tipo = tipo


#Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_zona_principal(self):
        return self.__zona_principal
    
    def get_nivel_sugerido(self):
        return self.__nivel_sugerido
    
    def get_tipo(self):
        return self.__tipo
    
    