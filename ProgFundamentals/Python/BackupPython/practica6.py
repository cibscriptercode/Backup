# Módulos: ------------------------------
# Forma 1: from modulos import funciones_matematicas as fm 
# Forma 2: from modulos.funciones_matematicas import *
# Forma 3: from modulos.funciones_matematicas import Ejemplo

#fm.sumar(1, 2)
#fm.restar(3, 2)

from modulos.funciones_matematicas import *

sumar(1, 2)
restar(1,2)

# Paquetes:  -----------------------------------------------------------
# Son carpetas que almacenan varios archivos comunes, similares a los paquetes en java
# Para que Python encuentre un paquete es nesesario que este tenga un archivo __init__.py

from paquete import modulo
modulo.potencia(2, 2)


# Paquetes distribuibles: ------------------------------------------------
# empaquetar nuestros modulos e instalarlos en cualquier ordenador: video 36, Pildoras Informáticas