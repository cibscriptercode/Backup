package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Restaurante;
import tap.tradizoneapp.service.RestauranteService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class RestauranteController {
    
    @Autowired
    private RestauranteService restauranteService;


    @PostMapping("/restaurantes")
    public Response<Restaurante> crearRestaurante(@RequestBody Restaurante restaurante){
        return restauranteService.crearRestaurante(restaurante);
    }

    @GetMapping("/restaurantes")
    public Response<Restaurante> getRestaurantes(){
        return restauranteService.getRestaurantes();
    }
}
