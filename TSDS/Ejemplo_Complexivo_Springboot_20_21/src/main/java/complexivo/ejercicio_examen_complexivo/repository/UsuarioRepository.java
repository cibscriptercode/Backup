package complexivo.ejercicio_examen_complexivo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import complexivo.ejercicio_examen_complexivo.model.Usuario;

@Repository
public interface UsuarioRepository extends JpaRepository<Usuario, Long>{
    
    Usuario findByUsername(String username);
    Usuario findByUsernameAndPassword(String username, String password);
}
