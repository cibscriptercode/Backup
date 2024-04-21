package tap.tradizoneapp.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tap.tradizoneapp.model.Producto;
import tap.tradizoneapp.service.ProductoService;
import tap.tradizoneapp.util.Response;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class ProductoController {
    
    @Autowired
    private ProductoService productoService;


    @PostMapping("/productos")
    public Response<Producto> crearProducto(@RequestBody Producto producto){
        return productoService.crearProducto(producto);
    }

    @GetMapping("/productos")
    public Response<Producto> getProductos(){
        return productoService.getProductos();
    }
}
