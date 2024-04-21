if 5 > 3 
    puts true
else
    puts false
end


if 5>3 && 6<2 
    puts(true) 
else 
    puts(false) 
end


if 4 == 5 
    puts true
elsif 5 > 3
    puts true
else
    puts false
end


puts "Hola mundo" unless false #se ejecuita solo cuando la exopresion es falsa.

#case --------------------------------------------------------------------------------------
print "dame tu calificacion: "
calificacion = gets.chomp.to_i

case calificacion
when 10
    puts "muy bien!"
when 9 
    puts "Casi"
else
    puts "q mal :'v"
end


puts case calificacion
when 10,9
    "muy bien!"
when 8,7
    "Casi"
else
    "q mal :'v"
end
