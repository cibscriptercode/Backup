# Pasos para conseguir conectar con una base de datos: ------------------------------------------
    # Abrir - Crear conexión.
    # Crear puntero.
    # Ejecutar una query.
    # Manejar los resultados de la query.
    # Cerrar puntero.
    # Cerrar conexión.
import sqlite3

conexion = sqlite3.connect("Sqlite3_db")
puntero = conexion.cursor()

puntero.execute("create table productos (nombre varchar(50), precio integer, seccion varchar(50))")
puntero.execute("insert into productos values ('balón', 10, 'Deportes')")

lista_productos = [ 
    ("Camiseta", 10, "Deportes"), 
    ("Jarron", 10, "Ceramica"), 
    ("Camión", 10, "Juguetería")
]

puntero.executemany("insert into productos values (?, ?, ?)", lista_productos)
puntero.execute("select * from productos")

productosdb = puntero.fetchall()

print(productosdb)

conexion.commit()
conexion.close()