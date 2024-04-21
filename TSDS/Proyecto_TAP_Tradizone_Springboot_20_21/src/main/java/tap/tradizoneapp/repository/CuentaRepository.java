package tap.tradizoneapp.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import tap.tradizoneapp.model.Cuenta;

@Repository
public interface CuentaRepository extends MongoRepository<Cuenta, String>{
    
}
