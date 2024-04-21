package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Local;
import tap.tradizoneapp.repository.LocalRepository;
import tap.tradizoneapp.util.Response;

@Service
public class LocalService {
    

    @Autowired
    private LocalRepository localRepository;

    public Response<Local> crearLocal(Local local){
        localRepository.insert(local);
        return new Response<>(201, "Recurso creado exitosamente!", null);
    }

    public Response<Local> getLocales(){
        return new Response<>(200, "Ok!", localRepository.findAll());
    }
}
