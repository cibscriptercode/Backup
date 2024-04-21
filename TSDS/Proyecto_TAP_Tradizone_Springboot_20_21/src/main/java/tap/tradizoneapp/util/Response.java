package tap.tradizoneapp.util;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@Setter
@Getter
@NoArgsConstructor
public class Response <T>{

    private int codigo;
    private String descripcion;
    private List<T> cuerpo;
}
