# Funciones lambda: -------------------------------------------
    # Su objetivo es minimizar las lineas de codigo de una funcion:
    # No siempre es posible transformar una función tradicional en una funcion lambda.
    # solo devuelven calculos, no se pueden usar bucles, ni condicionales en estas.
    # Solo para funciones muy simples.

def funcion_tradicional(base, altura):
    return (base*altura)/2

print(f"El area de un triangulo 5x6={funcion_tradicional(5, 6)}")


funcion_lambda = lambda base, altura: (base*altura)/2

print(f"El area de un triangulo 5x6={funcion_lambda(5, 6)}")

# Funcion Filter: -------------------------------------------
    # Pertenece a un grupo de funciones superiores pertenecienyttes al paradigma de programacion funcional.
    # Verifica que los elementos de una secuencia cumplan una condición, devolviendo un iterador con los
    # elementos que cumplan dicha condicion.

# Forma 1:
def get_pares(num):
    if num % 2 == 0:
        return True

lista_numeros = [1, 2, 3, 4, 5, 6]

print(list(filter(get_pares, lista_numeros)))

# Forma 2:
lista_pares = list(filter(lambda num: num % 2 == 0, lista_numeros))
print(lista_pares)


# Ejemplo 2:
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

salarios_altos = filter(lambda empleado: empleado.salario >= 400, lista_empleados)

for empleado in salarios_altos:
    print(empleado)