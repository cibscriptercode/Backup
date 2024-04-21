package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Producto;

@Repository
public interface ProductoRepository extends MongoRepository<Producto, String>{
    
}
