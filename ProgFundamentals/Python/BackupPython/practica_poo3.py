# Herencia: super e isinstance: -----------------
class Persona():

    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    
    def descripcion(self):
        print('Nombre: ', self.nombre, "Edad: ", self.edad, "Residencia: ", self.residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, residencia_emp):
        super().__init__(nombre_emp, edad_emp, residencia_emp)
        self.salario = salario
        self.antiguedad = antiguedad

    #Sobreescritura de métodos
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}.")


persona = Empleado(100, 5, 'Jorge', 25, 'Cuenca' )
print(f"persona es una instacia de Empleado: {isinstance(persona, Empleado)}")
    
