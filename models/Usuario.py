from datetime import date

class Usuario:
    
    __estado = None
    __nombre = None
    __email = None
    __telefono = None
    __username = None
    __password = None
    __fecha_nacimiento = None
    __fecha_registro = None
    __genero = None
    __altura_cm = None
    __peso_kg = None
    __perfil = None
    __rutina = []
    __lesion = []
    __equipamiento = []
    __objetivo = []

    def __init__(self, nombre, email, telefono, username, password, fecha_nacimiento, genero, altura_cm, peso_kg):
        raise RuntimeError
    
    @classmethod    
    def registrar(cls, nombre, email, telefono, username, password, fecha_nacimiento, genero, altura_cm, peso_kg):
        nuevo_usuario = cls.__new__(cls)
        nuevo_usuario.__estado = True
        nuevo_usuario.__nombre = nombre
        nuevo_usuario.__email = email
        nuevo_usuario.__telefono = telefono
        nuevo_usuario.__username = username
        nuevo_usuario.__password = password
        nuevo_usuario.__fecha_nacimiento = fecha_nacimiento
        nuevo_usuario.__fecha_registro = date.today()
        nuevo_usuario.__genero = genero
        nuevo_usuario.__altura_cm = altura_cm
        nuevo_usuario.__peso_kg = peso_kg
        nuevo_usuario.__perfil = None
        nuevo_usuario.__rutina = []
        nuevo_usuario.__lesion = []
        nuevo_usuario.__equipamiento = []
        nuevo_usuario.__objetivo = []
        return nuevo_usuario

#Setters
    def set_estado(self, estado):
        self.__estado = estado
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_username(self, username):
        self.__username = username

    def __set_password(self, password):
        self.__password = password

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_genero(self, genero):
        self.__genero = genero

    def set_altura_cm(self, altura_cm):
        self.__altura_cm = altura_cm

    def set_peso_kg(self, peso_kg):
        self.__peso_kg = peso_kg
    
    def set_perfil(self, perfil):
        self.__perfil = perfil
        
    def set_rutina(self, rutina):
        self.__rutina.append(rutina)
        
    def set_lesion(self, lesion):
        self.__lesion.append(lesion)
        
    def set_equipamiento(self, equipamiento):
        self.__equipamiento.append(equipamiento)
        
    def set_objetivo(self, objetivo):
        self.__objetivo.append(objetivo)

#Getters
    def get_estado(self):
        return self.__estado
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def get_username(self):
        return self.__username

    def __get_password(self):
        return self.__password

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_fecha_registro(self):
        return self.__fecha_registro

    def get_genero(self):
        return self.__genero

    def get_altura_cm(self):
        return self.__altura_cm

    def get_peso_kg(self):
        return self.__peso_kg
    
    def get_perfil(self):
        return self.__perfil
    
    def get_rutina(self):
        return self.__rutina
    
    def get_lesion(self):
        return self.__lesion
    
    def get_objetivo(self):
        return self.__objetivo
    
    def get_equipamiento(self):
        return self.__equipamiento
    
#Metodos

    def cambiar_estado(self):
        if self.get_estado() == True:
            self.set_estado(False)
        else:
            self.set_estado(True)
        
    def print_usuario(self):
        return print(f'''
                estado = {self.get_estado()}
                nombre = {self.get_nombre()}
                email = {self.get_email()}
                telefono = {self.get_telefono()}
                username = {self.get_username()}
                fecha nacimiento = {self.get_fecha_nacimiento()}
                fecha registro = {self.get_fecha_registro()}
                genero = {self.get_genero().name}
                altura en cm = {self.get_altura_cm()}
                peso en kg = {self.get_peso_kg()}
                perfil = {self.get_perfil}
                lesion = {self.get_lesion}
                equipamiento = {self.get_equipamiento}
                objetivo = {self.get_objetivo}
                     ''')
    
    def __autenticar_username(self, username):
        return (self.get_username() == username)
    
    def __autenticar_password(self, paswword):
        return (self.__get_password() == paswword)
    
    def autenticar(self, username, password):
        if (self.__autenticar_username(username) and self.__autenticar_password(password)):
            return print('Acceso validado')
        else:
            return print('Acceso denegado')
        
    def asignar_perfil(self, perfil):
        self.set_perfil(perfil)
        
    def asignar_rutina(self, rutina):
        self.set_rutina(rutina)
        
    def asignar_lesion(self, lesion):
        self.set_lesion(lesion)
        
    def asignar_objetivo(self, objetivo):
        self.set_objetivo(objetivo)
    
    def asignar_equipamiento(self, equipamiento):
        self.set_equipamiento(equipamiento)
    
    