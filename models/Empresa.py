class Empresa:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__usuarios = []
        
    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        
    def get_usuarios(self):
        return self.__usuarios
    
    def cantidad_usuarios_registrados(self):
        return len(self.__usuarios)
    