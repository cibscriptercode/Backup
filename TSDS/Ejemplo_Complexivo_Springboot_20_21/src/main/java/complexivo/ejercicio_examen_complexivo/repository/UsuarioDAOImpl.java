package complexivo.ejercicio_examen_complexivo.repository;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import complexivo.ejercicio_examen_complexivo.model.Usuario;

@Repository
public class UsuarioDAOImpl implements UsuarioDAO{

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Override
    public Usuario createUsuario(Usuario usuario) {
        return usuarioRepository.save(usuario);
    }

    @Override
    public Usuario recuperarPorUsername(String username) {
        return usuarioRepository.findByUsername(username);
    }

    @Override
    public List<Usuario> getUsuarios() {
        return usuarioRepository.findAll();
    }

    @Override
    public Usuario iniciarSesion(String username, String password) {
        return usuarioRepository.findByUsernameAndPassword(username, password);
    }
    
}
