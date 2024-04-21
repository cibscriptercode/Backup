# Matrices: cantidad de dimenciones, siempre los arreglos internos deben tener la misma cantidad de elementos.
# tienen una serie de operaciones matematicas mas amplias
# Matrix: todos los elementos deben ser numeros.

require 'matrix' #Para importaciones

matriz = [[1,2,3], [1,2,3]]
matriz = Matrix[[1,2,3], [1,2,3], [1,2,3]]

matriz.each do |i|
    puts i
end

matriz.each(:diagonal) do |i| #imprime la diagonal de una matriz
    puts i
end

