package practica.practica_cloudinary_pringboot.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

@Data
@Document(collection = "imagenes")
public class Imagen {
    
    @Id
    private String id;

    private String nombre;
    private String imgUrl;
    private String cloudinaryImgId;
}
