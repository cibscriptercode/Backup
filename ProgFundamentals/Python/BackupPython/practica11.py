# Funcion Match y search: ------------------------------------
import re

nombre_1 = 'Sandra López'
nombre_2 = 'Antonio Gómez'
nombre_3 = 'María López'

if re.match('Sandra', nombre_1, re.IGNORECASE) or re.match('.ara', nombre_1): # Busca el patron solo al inicio de la cadena.
    print('Se encontró el nombre.')
else:
    print('No se encontró el nombre.')


#La funcion search busca el patron en toda la cadena:
if re.search('López', nombre_1):
    print(nombre_1)