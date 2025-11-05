class Rutina_detalle:
    
    def __init__(self, dia_semana, series, repeticiones, duracion_min, peso_kg, nivel, observaciones):        
        self.__dia_semana = dia_semana
        self.__series = series
        self.__repeticiones = repeticiones
        self.__duracion_min = duracion_min
        self.__peso_kg = peso_kg
        self.__nivel = nivel
        self.__observaciones =observaciones



#Getters
    def get_dia_semana(self):
        return self.__dia_semana
    
    def get_series(self):
        return self.__series
    
    def get_repeticiones(self):
        return self.__repeticiones
    
    def get_duracion_min(self):
        return self.__duracion_min
    
    def get_peso_kg(self):
        return self.__peso_kg
    
    def get_nivel(self):
        return self.__nivel
    
    def get_observaciones(self):
        return self.__observaciones
    