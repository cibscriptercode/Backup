package practica.practica_cloudinary_pringboot.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import practica.practica_cloudinary_pringboot.entity.Imagen;
import practica.practica_cloudinary_pringboot.repository.ImagenRepository;

@Service
public class ImagenService {
    
    @Autowired
    private ImagenRepository imagenRepository;

    public List<Imagen> list(){
        return imagenRepository.findByOrderById();
    }


    public void save(Imagen imagen){
        imagenRepository.insert(imagen);
    }


    public void delete(String id){
        imagenRepository.deleteById(id);
    }

    public Optional<Imagen> getOne(String id){
        return imagenRepository.findById(id);
    }

    public boolean exists(String id){
        return imagenRepository.existsById(id);
    }
}
