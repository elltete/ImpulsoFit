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
from models.Perfil import Perfil
from models.Lesion import Lesion

user1 = Usuario.registrar("Tete", "email", 4444444, 'tete', 'abc123', "1974-06-29", Genero.MASCULINO, 174, 99)

perfil_user1 = Perfil(3, 2, 2, Lugar.CASA, Estilo_vida.ACTIVO, Tipo_ejercicio.FITNESS, "Natacion", Nivel.INTERMEDIO)

lesion1_user1 = Lesion('3', Zona_cuerpo.ESPALDA, Grado_lesion.MODERADO, 'Molestia', 'Lesion sin curar')



user1.asignar_perfil(perfil_user1)
user1.asignar_lesion(lesion1_user1)


print(user1.print_usuario())
user1.cambiar_estado()
print(user1.print_usuario())

user1.autenticar('tete', 'abc123')
user1.autenticar('tete2', 'abc123')
user1.autenticar('tete', 'abc1234')