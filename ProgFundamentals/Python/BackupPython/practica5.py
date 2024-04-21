# Excepciones: -----------------------
num1 = 8
num2 = 0
resultado = 0

try:
    resultado = num1/num2
except ZeroDivisionError:
    print('No se puede dividir un numero para cero')


try:
    resultado = num1/num2
except ZeroDivisionError:
    print('No se puede dividir un numero para cero')
except ValueError:
    print('No se puede transformar una letra en numero')
except:
    print('Error general')
finally:
    print('Se ejecutara siempre')

# Provocar intencionalmente una excepción:
def evalua_edad(edad):
    if 0<edad<18:
        return 'erres menor de edad'
    elif edad>=18:
        return 'eres mayor de edad'
    else:
        raise TypeError('No se permiten edades negativas')# Podemos escoger entre diferente tipos de errores.
