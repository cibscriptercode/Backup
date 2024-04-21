package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Local;
import tap.tradizoneapp.service.LocalService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class LocalController {
    
    @Autowired
    private LocalService localService;


    @PostMapping("/locales")
    public Response<Local> crearLocal(@RequestBody Local local){
        return localService.crearLocal(local);
    }

    @GetMapping("/locales")
    public Response<Local> getLocales(){
        return localService.getLocales();
    }
}
