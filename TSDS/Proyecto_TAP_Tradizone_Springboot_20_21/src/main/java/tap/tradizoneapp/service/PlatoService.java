package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Plato;
import tap.tradizoneapp.repository.PlatoRepository;
import tap.tradizoneapp.util.Response;

@Service
public class PlatoService {
    
    @Autowired
    private PlatoRepository platoRepository;

    public Response<Plato> crearPlato(Plato plato){
        platoRepository.insert(plato);
        return new Response<>(201, "Recurso creado exitosamente!", null);
    }

    public Response<Plato> getPlatos(){
        return new Response<>(200, "Ok!", platoRepository.findAll());
    }
}
