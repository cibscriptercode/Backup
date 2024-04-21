class Video

    attr_accessor :minutes, :title

    def initialize(title) #Una buena practica es no dejarle mucho trabajo al constructor.
        self.title = title
    end

end

video_1 = Video.new('Método Costructor')
puts video_1.title