package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.CategoriaProducto;

@Repository
public interface CategoriaProductoRepository extends MongoRepository<CategoriaProducto, String>{
    
}
