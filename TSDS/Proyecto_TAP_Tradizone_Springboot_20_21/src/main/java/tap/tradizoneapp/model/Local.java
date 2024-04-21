package tap.tradizoneapp.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import tap.tradizoneapp.util.Imagen;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
@Document(collection = "Locales")
public class Local {
    
    @Id
	private String id;

	private String avPrincipal;
	private String avSecundaria;
	private String latitud;
	private String altitud;
	private boolean estado;
	private int capacidad;
	private String diasLaborables;
	private String horarioJornada;
	private Imagen imagen;
}
