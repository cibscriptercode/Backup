# Funciones ----------------------------------

print('Hola mundo')

def saludar(nombre):
    return 'Hola '+nombre


def sumar(num1, num2):
    return num1+num2


print(saludar('Chriss'))

# Listas ----------------------------------
lista_frutas = ['Uva', 'Sandia', 'Banano']

print(lista_frutas[0])
print(lista_frutas[-1])

porcion_frutas = lista_frutas[0:2]
porcion_frutas.append('frutilla')
porcion_frutas.insert(2, 'Uvilla')
porcion_frutas.extend(['Pera', 'Manzana'])
posicion = porcion_frutas.index('Pera')

enLista = 'Manzana' in porcion_frutas

lista_diferentes_datos = [True, 'Perro', 5, 'String', False]
lista_diferentes_datos.remove('Perro')
lista_diferentes_datos.pop()

lista_total = lista_frutas + porcion_frutas

# Tuplas ----------------------------------
#  Son inmutables, no se puede agregar y eliminar
#  Se puede extraer porciones.
#  Si permite comprovar si un elemento se encuentra en ella.
#  Pueden utilizarse como claves en un diccionario.

tupla_1 = ("Jorge", "Juan")
tupla_1[0]
tupla_a_lista = list(tupla_1)
lista_a_tupla = tuple(lista_frutas)

"Jorge" in tupla_1
num = tupla_1.count("Jorge")
num_elementos = len(tupla_1)

tupla_unitaria = ("se debe colocar una coma para considararse una tupla",)

# Diccionarios ----------------------------------
diccionario = {'cleve_1': 'Alemania', 'clave_2': 'Reino Unido'}
diccionario['clave_1']
diccionario['clave_3'] = "EEUU"
del diccionario['clave_1']