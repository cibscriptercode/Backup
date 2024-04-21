# Trabajar con archivos externos: ------------------------------------------------------
# Crear -> abrir -> manipular -> cerrar
# Streams son flujos de datos que nos permiten trabajar con archivos externosen 2 direcciones
# es decir desde el programa hacia afuera y tambien desde fuera hacia el programa.
# los modods que tiene al abrir son de lectura(r), escritura(w) y modificacion(a).
from io import open

# Modo escritura: ............
archivo_texto = open('archivo.txt', "w")

frase = "Estupendo dia para estudiar python \n en martes"

archivo_texto.write(frase)

archivo_texto.close()

# Modo escritura: ............
archivo_texto = open('archivo.txt', "r")

lista_lineas_archivo = archivo_texto.readlines()

archivo_texto.close()

print(lista_lineas_archivo)

# Modo modificar(append): ............

archivo_texto = open('archivo.txt', "a")

archivo_texto.write("\n tercera linea")

archivo_texto.close()

# Desplazar la posicion del puntero: (por defecto siempre se situa al inicio del archivo en la primera linea)..........
archivo_texto = open('archivo.txt', "r")

# Desplaza el puntero nuevamente al inicio
archivo_texto.seek(0)

# Desplaza el puntero hasta el caracter 11.
archivo_texto.seek(11)

# Hace una lectura hasta el caracter 11
print(archivo_texto.read(11))

archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())

archivo_texto.close()

# Modo lectura y escritura: ............
archivo_texto = open('archivo.txt', "r+")

archivo_texto.write("comienzo del texto")

archivo_texto.seek(0)

lista_lineas_archivo = archivo_texto.readlines()

lista_lineas_archivo[1] = "Esta linea a sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_lineas_archivo)

archivo_texto.close()