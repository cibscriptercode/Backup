#Función Map: ----------------------------------------------------
    # Aplica una función a cada elemento de una lista iterable(listas, tuplas, etc)
    # devolviendo una lista con los resultados.
    # Esta funcion puede ser simple o compleja.

# Ejemplo:
class Empleado():
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return "{} trabaja como {} y tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)


lista_empleados = [
    Empleado('Jorge', 'Estibador', 400),
    Empleado('Ruth', 'Cargador', 300),
    Empleado('Ruben', 'Maquinista', 500),
    Empleado('Marco', 'Enfermero', 600),
    Empleado('Yaret', 'Lijador', 400),
    Empleado('McLovit', 'Psicologo', 300),
]

#A cada elemento le va a agregar un 3% de comicion si su salario es menor a 400$:
def calculo_comision(empleado):
    if empleado.salario < 400:
        empleado.salario = empleado.salario*1.03
    return empleado

lista_empleados = map(calculo_comision, lista_empleados)

for empleado in lista_empleados:
    print(empleado)


# Expresiones regulares: ----------------------------------------
    # Son una secuencia de caracteres que forman un patron de busqueda y sirven para el trabajo
    # y procesamiento de texto.

import re

cadena = "Aprendiendo expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
texto_buscar = 'Python'

if re.search('regulares', cadena) is not None:
    print('Esta palabara existe dentro del texto.')
else:
    print('Esta palabra no existe en el texto.')


print(f"el texto: {texto_buscar}, se encuentra {len(re.findall(texto_buscar, cadena))} veces en el texto.")

# Metacaracteres, caracteres comodín: -------------------------------------------

lista_nombres = ['Ana Gómez', 'María Martin', 'Sandra López', 'Santiago Martín']

for nombre in lista_nombres:
    # El caracter ^ filtra si lo que buscamos comienza por ese texto en este caso sandra.
    # El caracter $ filtra los que terminan en ese texto.
    if re.findall('^Sandra', nombre) and re.findall('López$', nombre):
        print(nombre)

    if re.findall('Mart[ií]n', nombre):
        print(nombre)

# Rangos en expresiones regulares: -------------------------------------------
for nombre in lista_nombres:
    # Filtra todos los nombres que contengan letras en tre un rango O a T 
    if re.findall('[O-T]', nombre):
        print(nombre)