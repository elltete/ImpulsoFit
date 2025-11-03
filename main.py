from utils.Estilo_vida import Estilo_vida
from utils.Lugar import Lugar
from utils.Tipo_ejercicio import Tipo_ejercicio
from utils.Genero import Genero
from utils.Grado_lesion import Grado_lesion
from utils.Meta import Meta
from utils.Nivel import Nivel
from utils.Tipo_equipamiento import Tipo_equipamiento
from utils.Zona_cuerpo import Zona_cuerpo
from models.Usuario import Usuario

user = Usuario.registrar("Tete2", "email", 4444444, 'tete', 'abc123', "1974-06-29", Genero.MASCULINO, 174, 99)

print(user.print_usuario())
user.cambiar_estado()
print(user.print_usuario())

user.autenticar('tete', 'abc123')
user.autenticar('tete2', 'abc123')
user.autenticar('tete', 'abc1234')