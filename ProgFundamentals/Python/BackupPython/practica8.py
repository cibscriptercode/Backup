# Serializacion: ------------------------------------------------------------------------
# consiste en guardar o almacenar un objeto coleccion o diccionario en un archivo o base 
# de dato en formato binario con el objetivo de distribuirlo o simplemente guardarlo.

import pickle 

lista_estudiantes = ['Sthefany', 'John', 'Andrea']

# modo escritura binaria: ............
fichero_binario = open('serializacion.txt', 'wb')

# Volcamos la lista en el archivo
pickle.dump(lista_estudiantes, fichero_binario)
fichero_binario.close()

# Elimina ese epacio en memoria
del(fichero_binario)

# modo electura binaria: ............
fichero = open('serializacion.txt', 'rb')

lista_estudiantes = pickle.load(fichero)

print(lista_estudiantes)

fichero.close()

# Guardado permanente: video 41 -> pildoras informaticas.