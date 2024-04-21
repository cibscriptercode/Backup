package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Restaurante;

@Repository
public interface RestauranteRepository extends MongoRepository<Restaurante, String>{
    
}
