package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Plato;

@Repository
public interface PlatoRepository extends MongoRepository<Plato, String>{
    
}
