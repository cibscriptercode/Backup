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
@Document(collection = "Recomendaciones")
public class Recomendacion {
    
    @Id
	private String id;
    
	private int rating;
	private boolean aprovacion;
	private String nombreUsuario;
}
