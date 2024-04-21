#Constantes siempre inician con una letra en mayuscula: ------------------------------------------------------
Constante_PI = 3.14

#Numeros: Enteros y Flotantes --> son objetos es decir tienen metodos que se ejecutan sobre ellos. -----------

entero = 7
flotante = 3.5

variable_ejm = entero.to_i #Convierte el numero en entero.
variable_ejm = entero.to_f #Convierte el numero en un flotante.
variable_ejm = entero.to_s #Convierte el numero en un string.


#Strings ------------------------------------------------------------------------------------------------------

cadena = "Esto es un String"

puts cadena * 5
puts "Hola pero #{cadena}" #interpolacion
cadena.length
cadena.upcase
cadena.capitalize
cadena.downcase
cadena.methods

#Entradas y Salidas: --------------------------------------------------------------------------------------------
print "Ingresar un numero: "
entrada = gets #Get String obtine solo strings.
numero = entrada.to_i

#Operadores en ruby: ---------------------------------------------------------------------------------------------
#Operadores Aritmeticos: +,-, *, /, %, potencia: **, 
#Operadores de Comparacion: <, >, >=, <=, !=, ==, metodo: eql?() evalua tanto el valor como el tipo de datos
#Operadores Lógicos: &&, ||, !

#Variables booleanas: --------------------------------------------------------------------------------------------
verdadero = true
falso = false

#Operador ternario: ----------------------------------------------------------------------------------------------
usuario = "Chriss"
puts(if usuario == "Chriss" then true else false end)
puts(usuario == "coco" ? true : false)


=begin
esto es un comentario multilinea
=end

