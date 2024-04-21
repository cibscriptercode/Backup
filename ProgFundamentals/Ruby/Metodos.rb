#Simbolos ---------------------------------------------------------------
#Es una cadena inmutable: significa que no se puede modificar la cadena en tiempo de ejecucion
#Su principal benefiecio esta en el performans ya que comparte el mismo object_id debido a que su contenido es igual.
simbolo1 = :simbolo_1
simbolo2 = :simbolo_2

# 1.- utilizar cuando no se necisite modificar el string, 2.- cuando no se nececite los métodos de string.
# 3.- son muy utiles como nombres de cosas, un ejemplo es usarlo como claves en hashes


# Métodos y argumentos en ruby -------------------------------------------
# se debe utilizar la palabra reservada return solo para romper la ejecucuion del metodo antes de la linea final del método
def cuadrado_de_un_numero(num) #La palabra reservada return puede omitirse, siempre retornan la ultima linea
    num*num
end

def saludar
    puts 'Hola Mundo!'
end

def sumar(num1, num2)
    return num1+num2
end


saludar()
puts cuadrado_de_un_numero(3)
puts "La suma es: #{sumar(3, 2)}"

# Operador splat --------------------------------------------------------
def hola_gente_1(personas)
    personas.each {|persona| puts "Hola #{persona}"}
end

hola_gente_1(['Uriel', 'coco'])

#Este método se escribe comunmente asi en ruby:
def hola_gente(*personas) #El operador splat dice que a este metodo se le puede pasar cualquier cantidad de argumentos y el los recibe como un arreglo.
    personas.each {|persona| puts "Hola #{persona}"} # Se puede mesclar con mas argumentos que sean fijos.
end

hola_gente('pedro', 23)

#Tambien se puede usar en sentido contrario es decir, convertir un array en una lista de argumentos.
nombres = %w['juan' 'pepito']
hola_gente(*nombres)

# Keywords Arguments: ----------------------------------------------------
def hola(nombre:"", edad:0, **multiples_valores) #asigna un valor por default al metodo. Parametros opcionales.
    if edad > 30
        puts "Hola señor #{nombre}"
    elsif edad < 30
        puts "Hola joven #{nombre}"
    end

    puts multiples_valores # Puede pasarle infinitos parametros que llegan un hash.
end

hola(nombre: "Juan", edad: 20, parametro_n: 'Mi color favorito es el rojo') #El orden de los parametros es arbitrario, se pueden pasar en el orden que se quiera.

def  hola_2(nombre:, apellido:) # Los argumentos son obligatorios.
    puts "#{nombre}, #{apellido}"
end

hola_2(nombre:'Juan', apellido: 'Martines')
