class Tutor


    def initialize(name)
        @name = name #Variables de Instancia no estan disponibles desde fuera del objeto solo dentro de este.
    end

    def say_my_name
        puts @name
    end

    #Métodos accesores ---> en ruby los metodos set y get no son usuados comno prefijo del nombre del método.
    def get_name
        @name
    end

    def set_name(name)
        @name = name
    end
end

uriel = Tutor.new('Uriel')
uriel.say_my_name
uriel.set_name('Ana')
puts uriel.get_name


# Métodos Accesores --------------------------------------

class Persona

    #setters y getters

    def name=(name)
        @name = name
    end

    def name
        @name
    end

end

ana = Persona.new
ana.name = "Ana"
puts ana.name


# Forma Optima de definir métodos Accesores ---------------------------------
 class Producto

    attr_accessor :nombre #Define tanto el getter como el setter
    attr_reader :nombre # define unicamente el getter 
    attr_writer :nombre # define unicamente el setter

 end

 producto_1 = Producto.new
 producto_1.nombre = 'Juan'
 puts producto_1.nombre


