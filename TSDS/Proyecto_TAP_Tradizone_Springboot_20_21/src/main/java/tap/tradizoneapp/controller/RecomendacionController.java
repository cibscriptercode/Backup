package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Recomendacion;
import tap.tradizoneapp.service.RecomendacionService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class RecomendacionController {
    
    @Autowired
    private RecomendacionService recomendacionService;


    @PostMapping("/recomendaciones")
    public Response<Recomendacion> crearRecomendacion(@RequestBody Recomendacion recomendacion){
        return recomendacionService.crearRecomendacion(recomendacion);
    }

    @GetMapping("/recomendaciones")
    public Response<Recomendacion> getRecomendaciones(){
        return recomendacionService.getRecomendaciones();
    }
}
