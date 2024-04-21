package tap.tradizoneapp.model;

import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.IndexDirection;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@NoArgsConstructor
@AllArgsConstructor
@Setter
@Getter
@Document(collection = "Restaurantes")
public class Restaurante {
    
    @Id
	private String id;
    
	private String nombreRestaurante;
    
	@Indexed(direction = IndexDirection.ASCENDING)
	private boolean estado;
	private String telefono;
	private Cuenta cuenta;
	private List<Local> locales;
}
