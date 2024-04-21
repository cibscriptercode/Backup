package tap.tradizoneapp.model;

import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
@Document(collection = "Platos")
public class Plato extends Producto{
    
	private String ingredientes;
	private String preparacion;
	private String historia;
}
