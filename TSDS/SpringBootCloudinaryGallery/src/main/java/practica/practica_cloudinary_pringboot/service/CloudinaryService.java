package practica.practica_cloudinary_pringboot.service;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import com.cloudinary.Cloudinary;
import com.cloudinary.utils.ObjectUtils;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public class CloudinaryService {
    
    private Cloudinary cloudinary;
    private Map<String, String> cloudinaryDataConfig = new HashMap<>();

    public CloudinaryService(){
        cloudinaryDataConfig.put("cloud_name", "divlnbpxa");
        cloudinaryDataConfig.put("api_key", "978698122616114");
        cloudinaryDataConfig.put("api_secret", "oyPtBqtBQPl7MfYLILp0g-v1BRM");
        cloudinary = new Cloudinary(cloudinaryDataConfig);
    }


    public Map upload(MultipartFile multipartFile)throws IOException {
        File file = convert(multipartFile);
        Map result = cloudinary.uploader().upload(file, ObjectUtils.emptyMap());//ObjectUtils.emptyMap() para decirle que no le agregue efectos especiales a la imagen.
        file.delete();
        return result;
    }


    public Map delete(String id)throws IOException {
        Map result = cloudinary.uploader().destroy(id, ObjectUtils.emptyMap());
        return result;
    }


    private File convert(MultipartFile multipartFile) throws IOException {
        File file = new File(multipartFile.getOriginalFilename());
        FileOutputStream fileWriter = new FileOutputStream(file);
        fileWriter.write(multipartFile.getBytes());
        fileWriter.close();
        return file;
    }
}
