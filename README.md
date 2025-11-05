# ImpulsoFit

Trabajo Práctico: Introducción a la IA y al Desarrollo de Sistemas

Materia: 	    Desarrollo De Sistemas De Inteligencia Artificial 

Profesor: 	    Matias Arellano

Institución: 	Instituto de Formación Técnica Superior Nº 12

Carrera: 	    Tecnicatura Superior en Ciencias de Datos e IA

Alumnos: 	    Leandro Pellegrini - pellegrini.leandro@hotmail.com
                Jonathan Rondon - biomed.jonathanrondon@gmail.com
		        Diego Ponzo - diegoponzo@gmail.com


Funcionalidades de un sistema sobre rutinas personalizadas de entrenamiento:

1. El sistema permitirá registrarse como USUARIO.

2. El usuario en el registro deberá ingresar su nombre, email, teléfono, usuario, contraseña, fecha de nacimiento, genero, altura y peso. 

3. El usuario deberá generar un PERFIL, donde debe indicar detalles de su vida personal, como por ejemplo dias disponible en la semana para entrenar, cantidad de dias semanales y horas disponible para el entrenamiento, lugar de entrenamiento (por ejemplo en casa, gimnasio, aire libre), estilo de vida (sedentario, activo, etc), que tipo de ejercicio le interesa realizar (ejemplo CrossFit, Running, Biking, Fitness, Gain, etc), si realiza alguna actividad física, su experiencia en entrenamiento.

4. El usuario debe indicar su OBJETIVO, detallando la meta de objetivo (por ejemplo perdida de grasa, ganar masa muscular, mejorar resistencia, estar bien fisicamente), el tiempo de alcance del objetivo.

4. El usuario deberá indicar si tiene LESIONES, que tipo de lesion, grado de dificultades, que zona del cuerpo es afectada, gravedad de la lesion.

5. El usuario deberá indicar que EQUIPAMIENTO dispone, por ejemplo bicicleta, mancuernas, soga, bandas, colchoneta, etc. 

6. Una vez que el usuario complete los puntos arriba mencionados, el sistema generara una RUTINA, teniendo en cuenta el PERFIL, el OBJETIVO, las LESIONES y el EQUIPAMIENTO del USUARIO. En dicha RUTINA, se mencionara los EJERCICIOS propuestos, indicando que dias, series, repeticiones, duración, nivel, peso y equipamiento a utilizar por cada EJERCICIO. 

7.  A medida que el usuario realiza el/los EJERCICIOS proporcionados en la RUTINA, el sistema generar un AVANCE del OBJETIVO.


Las funcionalidades implementadas son:

1- Registración - registrar():
Al registrarse un nuevo usuario, deberá ingresar su nombre, email, teléfono, nombre de usuario, contraseña, fecha de nacimiento, género, su altura y peso. 
Luego deberá generar su perfil, donde debe indicar cuantos dias disponibles en la semana tiene para entrenar, su frecuencia semanal, horas disponible para el entrenamiento, lugar de entrenamiento, su estilo de vida, que tipo de ejercicio le interesa realizar, si realiza alguna actividad física, y su experiencia en entrenamiento.
Deberá también indicar su objetivo de entrenamiento, detallando su meta, tiempo estimado de entrenamiento por semana, fecha de inicio del objetivo, y una descripción.
Debe indicar si tiene lesiones, para ello debe indicar qué tipo de lesión tiene, la zona del cuerpo afectada, el grado de la lesión y una observación.
Y por último, deberá indicar qué equipamiento posee.

2- 