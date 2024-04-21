package practica.practica_cloudinary_pringboot.controller;

import java.io.IOException;
import java.util.List;
import java.util.Map;

import javax.imageio.ImageIO;

import java.awt.image.BufferedImage;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import practica.practica_cloudinary_pringboot.dto.Mensaje;
import practica.practica_cloudinary_pringboot.entity.Imagen;
import practica.practica_cloudinary_pringboot.service.CloudinaryService;
import practica.practica_cloudinary_pringboot.service.ImagenService;

@RestController
@RequestMapping("/app")
@CrossOrigin("*")
public class MainController {
    
    @Autowired
    private CloudinaryService cloudinaryService;

    @Autowired
    private ImagenService imagenService;


    @GetMapping("/list")
    public ResponseEntity<List<Imagen>> list() {
        List<Imagen> list = imagenService.list();
        return new ResponseEntity<>(list, HttpStatus.OK);
    }


    @PostMapping("/upload")
    public ResponseEntity<?> upload(@RequestParam MultipartFile multipartFile) throws IOException{
        BufferedImage bi = ImageIO.read(multipartFile.getInputStream());
        
        if(bi == null){
            return new ResponseEntity<>(new Mensaje("imagen no valida!"), HttpStatus.BAD_REQUEST);
        }

        Map result = cloudinaryService.upload(multipartFile);
        Imagen imagen = new Imagen();
        imagen.setNombre((String)result.get("original_filename"));
        imagen.setImgUrl((String)result.get("url"));
        imagen.setCloudinaryImgId((String)result.get("public_id"));
        imagenService.save(imagen);
        return new ResponseEntity<>(new Mensaje("imagen Subida"), HttpStatus.CREATED);
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<?> delete(@PathVariable String id) throws IOException{
        if(!imagenService.exists(id)){
            return new ResponseEntity<>(new Mensaje("No existe la imagen"), HttpStatus.NOT_FOUND);
        }
        Imagen imagen = imagenService.getOne(id).get();
        Map result = cloudinaryService.delete(imagen.getCloudinaryImgId());
        imagenService.delete(id);
        return new ResponseEntity<>(new Mensaje("Imagen Eliminada"), HttpStatus.OK);
    }


}
