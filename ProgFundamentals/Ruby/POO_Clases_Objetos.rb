#Clases ---------------------------------
class Video

    attr_accessor :minutes, :title
    
    def play
    end

    def pause
    end

    def stop
    end
end

#Instancia u Objeto --------------------
video_1 = Video.new
video_1.title = "Clases y Objetos"
puts video_1.title



