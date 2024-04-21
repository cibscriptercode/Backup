package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Recomendacion;
import tap.tradizoneapp.repository.RecomendacionRepository;
import tap.tradizoneapp.util.Response;

@Service
public class RecomendacionService {
    
    @Autowired
    private RecomendacionRepository recomendacionRepository;


    public Response<Recomendacion> crearRecomendacion(Recomendacion recomendacion){
        recomendacionRepository.insert(recomendacion);
        return new Response<>(201, "recurso creado con exito!", null);
    }


    public Response<Recomendacion> getRecomendaciones(){
        return new Response<>(200, "Ok", recomendacionRepository.findAll());
    }
}
