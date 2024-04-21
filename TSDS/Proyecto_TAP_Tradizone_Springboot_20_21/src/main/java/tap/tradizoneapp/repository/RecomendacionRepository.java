package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Recomendacion;

@Repository
public interface RecomendacionRepository extends MongoRepository<Recomendacion, String>{
    
}
