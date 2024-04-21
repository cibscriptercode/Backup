# Clases y Objetos: ----------------------------------------------
class Coche():
    chasis = '0001'
    ruedas = 4
    en_marcha = False

    #self similar a this de otros lenguajes de programacion en los cuales el this ya esta implisito en los parametros
    # de la funcion y no es necesario colocarlo, sin embargo, en python lo tenemos que declarar explisitamente. 
    def metodo(self):
        pass# le dise a python que no tome en cuenta el codigo de esta funcion.

    def arrancar(self):
        self.en_marcha = True

    def get_estado(self):
        if self.en_marcha:
            print('El coche esta en marcha')
        else:
            print('El coche no esta en marcha')

mi_coche = Coche()#Instanciacion de clase o ejemplarizacion de clase o crear un objeto.
mi_coche.chasis
mi_coche.arrancar()

# Estado Inicial(constructores) y encapsulacion: ----------------------------------------------
class Persona():

    # Las propiedades comunes a todos los objetos se inicializan en el constructor.
    def __init__(self):
        self.__nombre = ""
        self.__cedula = "" # Si una propiedad comienza con 2 guiones bajos convierte a la propiedad en privada.

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    #Este metodo es privado.
    def __chequear_persona(self):
        self.examen_orina = 'OK'
        self.examen_heces = 'OK'
        print("La perona es saludable")

persona = Persona()


