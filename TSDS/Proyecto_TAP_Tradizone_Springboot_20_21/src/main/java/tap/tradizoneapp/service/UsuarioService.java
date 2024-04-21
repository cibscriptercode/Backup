package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Usuario;
import tap.tradizoneapp.repository.UsuarioRepository;
import tap.tradizoneapp.util.Response;

@Service
public class UsuarioService {
    
    @Autowired
    private UsuarioRepository usuarioRepository;


    public Response<Usuario> crearUsuario(Usuario usuario){
        usuarioRepository.insert(usuario);
        return new Response<>(201, "recurso creado con exito!", null);
    }


    public Response<Usuario> getUsuarios(){
        return new Response<>(200, "Ok", usuarioRepository.findAll());
    }

}
