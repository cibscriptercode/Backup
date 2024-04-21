package tap.tradizoneapp.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@Document(collection = "Usuarios")
public class Usuario {
    
    @Id
    private String id;

	private String nombres;
	private String apellidos;
	private String correo;
	private String celular;
}
