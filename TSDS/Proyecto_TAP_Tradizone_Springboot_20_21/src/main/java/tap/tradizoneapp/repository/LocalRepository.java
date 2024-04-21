package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Local;

@Repository
public interface LocalRepository extends MongoRepository<Local, String>{
    
}
