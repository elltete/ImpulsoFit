from utils.Estilo_vida import Estilo_vida
from utils.Lugar import Lugar
from utils.Tipo_ejercicio import Tipo_ejercicio
from utils.Genero import Genero
from utils.Grado_lesion import Grado_lesion
from utils.Meta import Meta
from utils.Nivel import Nivel
from utils.Tipo_equipamiento import Tipo_equipamiento
from utils.Zona_cuerpo import Zona_cuerpo
from models.Empresa import Empresa
from models.Usuario import Usuario
from models.Perfil import Perfil
from models.Lesion import Lesion
from models.Objetivo import Objetivo
from models.Equipamiento import Equipamiento

empresa = Empresa('ImpulsoFit')

#### Registracion de un usuario - INICIO###

user1 = Usuario.registrar('Nombre', 'email', '44444444', 'tete', 'abc123', '1974-06-29', Genero.MASCULINO, 174, 99)
empresa.agregar_usuario(user1)

perfil_user1 = Perfil(3, 2, 2, Lugar.CASA, Estilo_vida.ACTIVO, Tipo_ejercicio.FITNESS, "Natacion", Nivel.INTERMEDIO)
user1.asignar_perfil(perfil_user1)

objetivo_user1 = Objetivo(Meta.GANAR_MASA, 5, '2025-11-05', 'Aumentar 5kg de masa muscular')
user1.asignar_objetivo(objetivo_user1)

lesion1_user1 = Lesion(Zona_cuerpo.ESPALDA, Grado_lesion.MODERADO, 'Molestia en espalda zona baja')
lesion2_user1 = Lesion(Zona_cuerpo.PIERNA, Grado_lesion.LEVE, 'Leve lesion de pierna izquierda')
user1.asignar_lesion(lesion1_user1)
user1.asignar_lesion(lesion2_user1)

equipo1_user1 = Equipamiento(Tipo_equipamiento.BANDAS, 'Banda elastica firme')
equipo2_user1 = Equipamiento(Tipo_equipamiento.MANCUERNAS, 'Mancuernas de 5kg y 10k')
equipo3_user1 = Equipamiento(Tipo_equipamiento.COLCHONETA, 'Tamaño mediano')
user1.asignar_equipamiento(equipo1_user1)
user1.asignar_equipamiento(equipo2_user1)
user1.asignar_equipamiento(equipo3_user1)

#### Registracion de un usuario - FIN ###

user1.print_usuario()

#### Login de un usuario - Inicio ###

user1.autenticar('tete', 'abc123')
user1.autenticar('tete2', 'abc123')
user1.autenticar('tete', 'abc1234') 

#### Login de un usuario - FIN ###