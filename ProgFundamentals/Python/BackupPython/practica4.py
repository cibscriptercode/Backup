# Generadores: -------------------------------
    #Estructuras que extraen valores de una función y se almacenan en objetos iterables
    #que se pueden recorrer.

def funcion_tradicional_genera_pares(limite):
    num = 1
    lista_pares = []
    while num<limite:
        lista_pares.append(num*2)
        num+=1
    return lista_pares

print(funcion_tradicional_genera_pares(10))

def funcion_generadora_genera_pares(limite):
    num = 1
    while num < limite:
        yield num*2
        num+=1

objeto_generador = funcion_generadora_genera_pares(10)
print(next(objeto_generador))
print(next(objeto_generador))
print(next(objeto_generador))

# yield from: --------------------------------------
    # Simplifica el codigo de lo generadores  en el caso de utilizar bucles for anidados
    # *ciudades: permite recibir varios argumentos en forma de tupla.

def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        yield from ciudad #Devuelve una a una cada letra de la ciudad

ciudades_devueltas = devuelve_ciudades('Madrid', 'Paris')

