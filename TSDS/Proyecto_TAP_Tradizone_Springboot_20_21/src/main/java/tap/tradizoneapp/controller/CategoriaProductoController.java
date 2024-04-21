package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.CategoriaProducto;
import tap.tradizoneapp.service.CategoriaProductoService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class CategoriaProductoController {
    
    @Autowired
    private CategoriaProductoService categoriaService;


    @PostMapping("/categorias")
    public Response<CategoriaProducto> crearCategoria(@RequestBody CategoriaProducto categoria){
        return categoriaService.crearCategoria(categoria);
    }

    @GetMapping("/categorias")
    public Response<CategoriaProducto> getCategorias(){
        return categoriaService.getCategorias();
    }
}
