package tap.tradizoneapp.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import tap.tradizoneapp.util.Imagen;

@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@Document(collection = "Cuentas")
public class Cuenta {
    
    @Id
	private String id;
    
	private String nombreUsuario;
	private String passwordUsuario;
	private boolean estado;
	private Imagen imagen;
	private Usuario usuario;
}
