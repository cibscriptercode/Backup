fn imprimir_ciclos(contexto: &str){
    for _ in 0..5{
        println!("{} {} {}", contexto, ", para los ciclos N°", i+1);
    }
}

fn main(){
    println!("Hola mundo desde Rust!\n");
    let contexto = "Este apartado del repositorio esta dedicado al aprendizaje de la carrera Tecnologia Superior en Mecatronica";
    imprimir_ciclos(contexto);
}
