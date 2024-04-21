import sqlite3

conexion = sqlite3.connect("sqlite3_db")
cursor = conexion.cursor()

cursor.execute(
    '''
    create table productos(
        codigo varchar(4) primary key,
        nombre varchar(50) unique,
        precio integer,
        seccion varchar(50)
    )
    '''
)


productos = [
    ('AR01', 'PELOTA', 20, 'DEPORTES'),
    ('AR02', 'PANTALÓN', 25, 'CONFECCIÓN'),
    ('AR03', 'DESTORNILLADOR', 5, 'FERRETERIA'),
    ('AR04', 'JARRÓN', 100, 'CERAMICA'),
    ('AR05', 'CAMISETA', 25, 'CONFECCIÓN')
]

cursor.executemany("insert into productos values (?,?,?,?)", productos)

cursor.execute("select * from productos where seccion = 'CONFECCIÓN'")
productos = cursor.fetchall()
print(productos)


cursor.execute("update productos set precio = 35 where nombre = 'PELOTA'")
cursor.execute("delete from productos where nombre = 'CAMISETA'")

conexion.commit()
conexion.close()