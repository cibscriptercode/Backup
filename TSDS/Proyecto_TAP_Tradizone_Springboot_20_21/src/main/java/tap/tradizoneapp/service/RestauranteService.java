package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Restaurante;
import tap.tradizoneapp.repository.RestauranteRepository;
import tap.tradizoneapp.util.Response;

@Service
public class RestauranteService {
    
    @Autowired
    private RestauranteRepository restauranteRepository;


    public Response<Restaurante> crearRestaurante(Restaurante restaurante){
        restauranteRepository.insert(restaurante);
        return new Response<>(201, "recurso creado con exito!", null);
    }


    public Response<Restaurante> getRestaurantes(){
        return new Response<>(200, "Ok", restauranteRepository.findAll());
    }
}
