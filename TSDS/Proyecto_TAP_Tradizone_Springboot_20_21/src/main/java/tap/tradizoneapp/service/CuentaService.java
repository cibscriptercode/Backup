package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Cuenta;
import tap.tradizoneapp.repository.CuentaRepository;
import tap.tradizoneapp.util.Response;


@Service
public class CuentaService {
    
    @Autowired
    private CuentaRepository cuentaRepository;


    public Response<Cuenta> crearCuenta(Cuenta cuenta){
        cuentaRepository.insert(cuenta);
        return new Response<>(201, "Recurso creado exitosamente!", null);
    }

    public Response<Cuenta> getCuentas(){
        return new Response<>(200, "Ok!", cuentaRepository.findAll());
    }
}
