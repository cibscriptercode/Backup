# Ciclo while: se ejecutra mientras sea verdadero-------------------------------
es_falso = false
i = 0
while i < 10
    puts i
    puts es_falso
    i+=1
    es_falso = true if i == 8
    es_falso != 0
end


# Until se ejecuta mientras sea falso y se lee 'hasta que'-----------------------
i = 0
until i == 10
    print i
    i+=1
end

# Do While ----------------------------------------------------------------------
i = 0
begin
    print " #{i}"
    i+=1
end while i<10

# Iteradores: Un iterador es un metodo que internamente construye un ciclo, este ciclo tiene caracteristicas especificas
# y nos permite invocar un bloque basado en estas caracteristicas dentro de un ciclo

# Times:
10.times do |i| # Genera numeros desde el cero
    puts i
end

10.times do
    puts "Me ejecutare 10 veces"
end


# Upto
1.upto(10) do |i|
    puts i
end


# Downto

10.downto(1) do |i|
    puts i
end

