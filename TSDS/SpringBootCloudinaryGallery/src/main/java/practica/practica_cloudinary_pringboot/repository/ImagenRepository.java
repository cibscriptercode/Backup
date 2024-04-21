package practica.practica_cloudinary_pringboot.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import practica.practica_cloudinary_pringboot.entity.Imagen;

@Repository
public interface ImagenRepository extends MongoRepository<Imagen, String>{
    
    public List<Imagen> findByOrderById();
}
