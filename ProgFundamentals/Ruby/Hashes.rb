# Tambien son llamados arreglos asociativos. la clave puede ser cualquier tipo de objeto
tutor = {'clave' => 'valor', 'clave_2' => 'valor_2'}
tutor.default = ":'v" # Valor por defecto para claves que no existen.

puts tutor
puts tutor['clave_2']
puts tutor['valor que no existe']

# Sintaxcis de hashes mas  utilizada es que la clave se un simbolo

arreglo_asociativo = {:clave_1 => 'valor_1', :clave_2 => 'valor_2'}
puts arreglo_asociativo

# Otras sintaxis, esta es la mas legible y facikl de leer
arreglo_asociativo = {clave_1: 'valor_1', clave_2: 'valor_2'} # utilizar simbolos para buscar elementos
puts arreglo_asociativo

arreglo_asociativo.each do |clave, valor|
    puts "En la clave: #{clave}, esta el valor: #{valor}"
end

# Operaciones con hashes:
arreglo_asociativo.length # Tambien con el metodo size()
puts arreglo_asociativo.has_key?("clave") #devuelve true si existe esa clave dentro del hash
arreglo_asociativo.keys # devuelve un arreglo con todas las claves
arreglo_asociativo.values # devuelve todos los valores del hash en un array
arreglo_asociativo.delete(:clave_1)
arreglo_asociativo.empty?
arreglo_asociativo.key("valor_2") #devuelve la clave de ese valor
arreglo_asociativo.has_value?('valor_3')
arreglo_asociativo.invert #invierte las claves y los valores
