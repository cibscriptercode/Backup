# Polimorfimo es el concepto en POO que describe la habilidad de que multiples objetos respondan de maneras distintas al mismo mensaje.
class Video
    def play
        #no implementado
    end
end


class Vimeo 
    def play
        p "inserta el reproductor de vimeo"
    end
end

class Youtube 
    def play
        p "inserta el reproductor de Youtube"
    end
end

videos = [Youtube.new, Vimeo.new, Vimeo.new, Vimeo.new, Vimeo.new]

videos.each do |video|
    video.play
end

# Esta estrechamente ligado a la herencia y a las interfaces, sin embargo en ruby no existen klas interfaces, existe el concepto de duckTyping
# duckTyping: si algo se ve comoi pato, suena como pato, camina como pato entonces debe ser un pato.
# No importa el tipo de dato, si puede hacer una accion la hara.
#Esto quiere decir que no importa que sean clases diferentes, no depende de herencias ni interfaces.

