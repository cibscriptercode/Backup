# Estructura condicional if elese: -----------------------------------
def evaluar(nota):
    valoracion = 'aprovado'
    if nota < 5:
        valoracion = 'reprovado'
    else:
        valoracion = 'aprovado'
    return valoracion


evaluacion = False
nota = int(input())

if evaluacion and nota < 10:
    respuesta = "reprovado"
elif not evaluacion or nota >= 10:
    respuesta = 'aprovado'
else:
    respuesta = 'no se puede calificar'


# Concatenacion de operadores de comparación: -----------------------
edad = 7

if 0<edad<18:
    respuesta = 'es menor de edad'
