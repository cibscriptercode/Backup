package tap.tradizoneapp.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import tap.tradizoneapp.model.CategoriaProducto;
import tap.tradizoneapp.repository.CategoriaProductoRepository;
import tap.tradizoneapp.util.Response;

@Service
public class CategoriaProductoService {
    
    @Autowired
    private CategoriaProductoRepository categoriaRepository;

    public Response<CategoriaProducto> crearCategoria(CategoriaProducto categoria){
        categoriaRepository.insert(categoria);
        return new Response<>(201, "Recurso creado exitoamente!", null);
    }

    public Response<CategoriaProducto> getCategorias(){
        return new Response<>(200, "Ok!", categoriaRepository.findAll());
    }
}
