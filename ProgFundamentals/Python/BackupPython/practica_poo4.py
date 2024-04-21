#Polimorfismo: ----------------------------------------------
    #Un objeto puede cambiar de forma dependiendo del contexto, puede cambiar su comportamiento.

class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas')


class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas')


class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando 6 ruedas')


def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()


mi_vehiculo = Camion()
desplazamiento_vehiculo(mi_vehiculo)