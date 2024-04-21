# Decoradores: -------------------------------------------------------------------
    # Son funciones que añaden funcionalidades a otra funciones.
    # Esta formado por 3 funciones(A,B,C) donde A recibe como parametro a B para devolver C.
    # Un decorador devuelve una función.
    # Esto sirve si queremos añadir funcionalidad extra a varias funciones.
    # Ejemplo:
"""
    def función_decorador(función):
        def función_interna():
            #Código de la función interna.
        return función_interna
"""

def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        # Acciones adicionales que decoran:
        print("vamos a realizar un calculo.")
        # Accion de la funcion decorada, en este caso sumar() o restar().
        funcion_parametro()
        # Acciones adicionales que decoran:
        print('Hemos terminado el calculo.')
    return funcion_interna()


@funcion_decoradora
def sumar():
    print(5+6)

@funcion_decoradora
def restar():
    print(5-6)

# Decoradores con parametros: -----------------------------------------------------
def funcion_decoradora_con_params(funcion_parametro):
    def funcion_interna(*args): # *args hace referencia a que puede recibir un conjunto extenso de parametros El nombre args es solo una convencion.
        print("Acciones decoradoras")
        funcion_parametro(*args)
        print("Otras acciones decoradoras")
    return funcion_interna

@funcion_decoradora_con_params
def hacer_suma(num1, num2):
    print(num1+num2)

hacer_suma(1, 2)



# Decoradores con argumentos clave, valor: ----------------------------------------
def decorador_clave_valor(funcion_parametro):
    def funcion_interna(*args, **kwargs): # *args hace referencia a que puede recibir un conjunto extenso de parametros El nombre args es solo una convencion.
        print("Acciones decoradoras")
        # **kwargs se coloco cuando queremos que los argumentos de una funcion tengan como clave el nombre de la variable.
        funcion_parametro(*args, **kwargs)
        print("Otras acciones decoradoras")
    return funcion_interna


@decorador_clave_valor
def potencia(base, exponente):
    print(pow(base, exponente))

potencia(base=2, exponente=2)