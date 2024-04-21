package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.Producto;
import tap.tradizoneapp.repository.ProductoRepository;
import tap.tradizoneapp.util.Response;

@Service
public class ProductoService {
    
    @Autowired
    private ProductoRepository productoRepository;


    public Response<Producto> crearProducto(Producto producto){
        productoRepository.insert(producto);
        return new Response<>(201, "recurso creado con exito!", null);
    }


    public Response<Producto> getProductos(){
        return new Response<>(200, "Ok", productoRepository.findAll());
    }
}
