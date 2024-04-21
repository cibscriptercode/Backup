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
import tap.tradizoneapp.util.Imagen;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
@Document(collection = "Productos")
public class Producto {
    
    @Id
	private String id;
    private String nombre;

    @Indexed(direction = IndexDirection.ASCENDING)
    private String descripcion;
    private boolean estado;
	private double precio;
	private Imagen imagen;
	private Restaurante restaurante;
	private List<CategoriaProducto> categorias;
	private List<Recomendacion> recomendaciones;
}
