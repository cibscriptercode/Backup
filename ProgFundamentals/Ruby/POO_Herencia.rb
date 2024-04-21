#Todos los objetos que creamos heredan de Object. Clase Padre de todas las clases.
class Video
    attr_accessor :title, :duration

    def metodo_para_sobreescribir
        puts 'Yo soy el padre'
    end

    def setup(name)
        @title = title
        puts "Lógica del padre + el titulo que viene de super #{@title}"
    end
end

class YoutubeVideo < Video #YoutubeVideo hereda de Video
    attr_accessor :youtube_id

    def metodo_para_sobreescribir #Sobre escritura de métodos.
        puts 'Yo soy el hijo'
    end

    def setup(name)
        super
        # Logica para hacer sin perder lo q ya hacia el padre}
        puts "nueva lógica ...."
    end
end

video1 = YoutubeVideo.new
video1.title = 'Un video'
puts video1.title
video1.metodo_para_sobreescribir
video1.setup('Video 1')
puts video1.object_id