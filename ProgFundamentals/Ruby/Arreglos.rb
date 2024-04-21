# Arreglos: ----------------------------------------------------------------------------------------------------------------------------------

arreglo = [3, 'perro', true] #Con elementos
arreglo_2 = Array.new(5) #vacio
arreglo_3 = %w[1 2 4 5 7] #permite agregar elementos sin nececidad de colocar la coma, es decir se usa el espacio para separar elementos.

arreglo << 'Este elemento se inserta en el elemento arreglo, << es similar a una funcion de añadir add()'

puts arreglo
puts arreglo_2


puts arreglo[3] #Inicia desde la posicion cero.

# Each: --------------------------------------------------------------------------------------------------------------------------------------
calificaciones = %w[10 4 6 8 9 0] #al escribir los array de esta forma los transforma en cadenas.

puts calificaciones
print calificaciones

suma = 0
calificaciones.each do |elemento|
    suma += elemento.to_f
end

puts "El promedio de tus calificaciones es: #{suma/calificaciones.length}" #tambien se puede utilizar la funcion size()

calificaciones.each_with_index do |elemento, indice|
    puts "la calificación: #{elemento} esta en la posición: #{indice}"
end


#Operaciones con Arreglos: -------------------------------------------------------------------------------------------------------------------

calificaciones = [10, 4, 6, 8, 9, 0]

calificaciones*2 #Duplica el arrelo
puts calificaciones*'-' #debuelve una cadena separada por -
calificaciones.join('-')#Igual al anterior, podemos utilizar diferentes formas de hacerlo

print calificaciones.sort #Ordena de menor a mayor
print calificaciones.sort.reverse #Ordena de mayor a menor.
print calificaciones.reverse #revierte el orden de los elementos.

puts calificaciones.include?(10) #Retorna true si existe ese elemento en el arreglo.
puts calificaciones.first #Devuelve el primer elemento.
puts calificaciones.last #Devuelve el ultimo elemento.
puts calificaciones.uniq #DEvuelve un arreglo si elementos repétidos.
puts "Devuelveme un elemento random del arreglo: #{calificaciones.sample}"

# Rangos: -------------------------------------------------------------------------------------------------------------------------------------
numeros = (1..10) #genera un array con numeros del uno al 10.
numeros.step(2).each do |elemento| end #Itera el arreglo de 2 en 2

('a'..'z').each do |elemento|
    print elemento+', '
end

arreglo_str = ('a'..'z').to_a #Convierte el rango en una arreglo.

# Comparte la mayor parte de metodos de los arreglos.
    
puts ('PRO001'..'PRO009').to_a #Puede generar rangos inteligentemente.
