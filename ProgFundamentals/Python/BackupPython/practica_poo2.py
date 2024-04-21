# Herencia: ---------------------------------------------
class Vehiculo():
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print('Vehiculo arranca')

    def acelerar(self):
        print('Vehiculo acelera')

    def frenar(self):
        print('Vehiculo frena')

    # la sobrescritura en python consite en escribir nuevamente el metodo igual que el anterior.

class Moto(Vehiculo):
    pass

moto = Moto('Honda', 'Pilot')
moto.acelerar()

# Herencia Multiple: ---------------------------------------------
class VehiculosElectricos():
    def __init__(self, autonomia):
        self.autonomia = autonomia

class VicicletaElectrica(VehiculosElectricos ,Vehiculo):
    pass

