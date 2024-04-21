package complexivo.ejercicio_examen_complexivo.repository;

import java.util.List;

import complexivo.ejercicio_examen_complexivo.model.Usuario;

public interface UsuarioDAO {
    
    Usuario createUsuario(Usuario usuario);
    Usuario recuperarPorUsername(String username);
    List<Usuario> getUsuarios();
    Usuario iniciarSesion(String username, String password);
}
