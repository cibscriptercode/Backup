#Alcance de los métodos: publicos privados y protegidos --> c0onocido como scope o alcance de una variable o método.
#Por defecto todos los métodos son publicos.
#Las clases hijas tambien pueden llamar a los metodos privados y protegidos.

class  Humano

    def publico
        puts 'soy publico'
    end

    private 
        def privado
            puts 'soy privado'
        end

    protected
        def protegido
            puts 'soy protegido'
        end
end

class Tutor < Humano
end

# Metodos de Clase: Las clase de ruby tambien son un objeto. ----------------------------------------------------
class SoyUnObjetoLoJuro
    @nombre_clase = 'SoyUnObjetoLoJuro' #si se define por fuera entonces le pertenece a la clase, si se define en un metodo le pertenece al método.

    def self.nombre_clase # Este es un método estatico
        @nombre_clase
    end

    def self.nombre_clase=(nombre_clase) # Este es un método estatico setter
        @nombre_clase = nombre_clase
    end

    class << self
        def metodo_estatico
            puts 'Otra forma de definir métodos estaticos.'
        end
    end
end

SoyUnObjetoLoJuro.nombre_clase = "No me cambien el nombre porfa!! :v"
puts SoyUnObjetoLoJuro.nombre_clase
SoyUnObjetoLoJuro.metodo_estatico

# Variables de clase. -------------------------------------------------------------------------------------------------
class Video
    @@type = 'video/mp4' # pueden ser accedidas desde métodos de la clase y métodos del objeto --> estaticas

    def self.type_desde_clase
        p @@type
    end

    def type_desde_objeto
        p @@type
    end
end

Video.type_desde_clase
Video.new.type_desde_objeto