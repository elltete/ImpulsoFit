class Objetivo:
    
    def __init__(self, meta, tiempo_estimado_semanas, fecha_inicio, descripcion):
        self.__meta = meta
        self.__tiempo_estimado_semanas = tiempo_estimado_semanas
        self.__activo = True
        self.__fecha_inicio = fecha_inicio
        self.__porcentaje_cumplido = 0
        self.__descripcion = descripcion

#Getters
    def get_meta(self):
        return self.__meta
    
    def get_tiempo_estimado_semanas(self):
        return self.__tiempo_estimado_semanas
    
    def get_horas_disponibles(self):
        return self.__activo
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_porcentaje_cumplido(self):
        return self.__porcentaje_cumplido

    def get_descripcion(self):
        return self.__descripcion

    def _set_porcentaje_cumplido(self, valor):
        self.__porcentaje_cumplido = valor
    
    
    def actualizar_porcentaje_cumplido(self, valor):
        self._set_porcentaje_cumplido(valor)