class Perfil:
    
    def __init__(self, dias_disponibles, frecuencia_semanal, horas_disponibles, lugar_entrenamiento, estilo_vida, tipo_de_interes, actividad_actual, experiencia):
        self.__dias_disponibles = dias_disponibles
        self.__frecuencia_semanal = frecuencia_semanal
        self.__horas_disponibles = horas_disponibles
        self.__lugar_entrenamiento = lugar_entrenamiento
        self.__estilo_vida = estilo_vida
        self.__tipo_de_interes = tipo_de_interes
        self.__actividad_actual = actividad_actual
        self.__experiencia = experiencia


#Getters
    def get_dias_disponibles(self):
        return self.__dias_disponibles
    
    def get_frecuencia_semanal(self):
        return self.__frecuencia_semanal
    
    def get_horas_disponibles(self):
        return self.__horas_disponibles
    
    def get_lugar_entrenamiento(self):
        return self.__lugar_entrenamiento
    
    def get_estilo_vida(self):
        return self.__estilo_vida

    def get_tipo_de_interes(self):
        return self.__tipo_de_interes
    
    def get_actividad_actual(self):
        return self.__actividad_actual
    
    def get_experiencia(self):
        return self.__experiencia
    
    def print_perfil(self):
        return(
            f'''
                dias_disponibles = {self.__dias_disponibles}
                frecuencia_semanal = {self.__frecuencia_semanal}
                horas_disponibles = {self.__horas_disponibles}
                lugar_entrenamiento = {self.__lugar_entrenamiento.name}
                estilo_vida = {self.__estilo_vida.name}
                tipo_de_interes = {self.__tipo_de_interes.name}
                actividad_actual = {self.__actividad_actual}
                experiencia = {self.__experiencia.name}
            '''
        )
 