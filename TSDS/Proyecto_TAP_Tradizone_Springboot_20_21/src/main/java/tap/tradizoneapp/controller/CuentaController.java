package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Cuenta;
import tap.tradizoneapp.service.CuentaService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class CuentaController {
    
    @Autowired
    private CuentaService cuentaService;

    
    @PostMapping("/cuentas")
    public Response<Cuenta> crearCuenta(@RequestBody Cuenta cuenta){
        return cuentaService.crearCuenta(cuenta);
    }


    @GetMapping("/cuentas")
    public Response<Cuenta> getCuentas(){
        return cuentaService.getCuentas();
    }
}
