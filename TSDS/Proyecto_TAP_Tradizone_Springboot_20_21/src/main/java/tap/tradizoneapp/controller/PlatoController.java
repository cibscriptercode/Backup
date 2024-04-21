package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Plato;
import tap.tradizoneapp.service.PlatoService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class PlatoController {
    
    @Autowired
    private PlatoService platoService;


    @PostMapping("/platos")
    public Response<Plato> crearPlato(@RequestBody Plato plato){
        return platoService.crearPlato(plato);
    }

    @GetMapping("/platos")
    public Response<Plato> getPlatos(){
        return platoService.getPlatos();
    }
}
