from tkinter import *
from tkinter import messagebox
import sqlite3

# FUNCIONES: ---------------------------------------
def conexion_db():
    try:
        conexion = sqlite3.connect('practica_guiada_db')
        cursor = conexion.cursor()
        cursor.execute(
            '''
            create table usuarios(
                id integer primary key autoincrement,
                nombre varchar(20),
                contrasena varchar(20),
                apellido varchar(20),
                direccion varchar(50),
                comentarios varchar(100)
            )
            '''
        )
        messagebox.showinfo('BD', "Base de datos creada con exito!")
    except:
        messagebox.showwarning('¡Atencion!', "¡La Base de datos ya existe!")


def cerrar_aplicacion():
    desicion = messagebox.askquestion("Salir", "¡Desea salir de la aplicación!")
    if desicion == 'yes':
        root.destroy()


def limpiar_campos_txt():
    id.set("")
    nombre.set("")
    contrasena.set("")
    apellido.set("")
    direccion.set("")
    txta_comentario.delete(1.0, END)


def crear_usuario():
    conexion = sqlite3.connect('practica_guiada_db')
    cursor = conexion.cursor()
    """cursor.execute(
        f'''insert into usuarios values(
                null, 
                '{nombre.get()}', 
                '{contrasena.get()}',
                '{apellido.get()}',
                '{direccion.get()}',
                '{txta_comentario.get("1.0", END)}'
            )
        '''
    )"""
    datos_usuario = nombre.get(), contrasena.get(), apellido.get(), direccion.get(), txta_comentario.get("1.0", END)
    cursor.execute("insert into usuarios values(null, ?, ?, ?, ?, ?)", datos_usuario)
    conexion.commit()
    messagebox.showinfo("Info:", "¡Registro creado con exito!")


def get_usuario():
    conexion = sqlite3.connect('practica_guiada_db')
    cursor = conexion.cursor()
    cursor.execute(f"select * from usuarios where id = {id.get()}")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        id.set(usuario[0])
        nombre.set(usuario[1])
        contrasena.set(usuario[2])
        apellido.set(usuario[3])
        direccion.set(usuario[4])
        txta_comentario.insert(1.0, usuario[5])
    conexion.commit()


def actualizar_usuario():
    conexion = sqlite3.connect('practica_guiada_db')
    cursor = conexion.cursor()
    cursor.execute(
        f'''update usuarios set 
            nombre = '{nombre.get()}',
            contrasena = '{contrasena.get()}',
            apellido = '{apellido.get()}',
            direccion = '{direccion.get()}',
            comentarios = '{txta_comentario.get("1.0", END)}'
            where id = '{id.get()}'
        '''
    )
    conexion.commit()
    messagebox.showinfo("Info:", "¡Actualizado con exito!")

def eliminar_usuario():
    conexion = sqlite3.connect('practica_guiada_db')
    cursor = conexion.cursor()
    cursor.execute(f"delete from usuarios where id = '{id.get()}'")
    conexion.commit()
    messagebox.showinfo("Info:", "¡Eliminado con exito!")

# CREACION DE LA INTERFAZ GRAFICA: ---------------------------------------

root = Tk()

# CREACION DEL MENU: ---------------------------------------
menu_principal = Menu(root)
root.config(menu=menu_principal, width=300, height=300)

menu_bd = Menu(menu_principal, tearoff=0)
menu_bd.add_command(label="Conectar", command=conexion_db)
menu_bd.add_command(label="Salir", command=cerrar_aplicacion)

menu_limpiar = Menu(menu_principal, tearoff=0)
menu_limpiar.add_command(label="Limpiar Campos", command=limpiar_campos_txt)

menu_crud = Menu(menu_principal, tearoff=0)
menu_crud.add_command(label="Crear", command=crear_usuario)
menu_crud.add_command(label="Leer", command=get_usuario)
menu_crud.add_command(label="Actualizar", command=actualizar_usuario)
menu_crud.add_command(label="Eliminar", command=eliminar_usuario)


menu_principal.add_cascade(label="DDBB", menu=menu_bd)
menu_principal.add_cascade(label="Limpiar", menu=menu_limpiar)
menu_principal.add_cascade(label="CRUD", menu=menu_crud)


# CREACION DE LOS CAMPOS DEL USUARIO: ---------------------------------------
frame_usuario = Frame(root)
frame_usuario.pack()

id = StringVar()
nombre = StringVar()
contrasena = StringVar()
apellido = StringVar()
direccion = StringVar()

txt_id = Entry(frame_usuario, textvariable=id)
txt_nombre = Entry(frame_usuario, textvariable=nombre)
txt_contrasena = Entry(frame_usuario, textvariable=contrasena)
txt_apellido = Entry(frame_usuario, textvariable=apellido)
txt_direccion = Entry(frame_usuario, textvariable=direccion)
txta_comentario = Text(frame_usuario, width=16, height=5)
scroll_vertical = Scrollbar(frame_usuario, command=txta_comentario.yview)


txt_id.grid(row=0, column=1, padx=10, pady=10)
txt_nombre.grid(row=1, column=1, padx=10, pady=10)
txt_contrasena.grid(row=2, column=1, padx=10, pady=10)
txt_apellido.grid(row=3, column=1, padx=10, pady=10)
txt_direccion.grid(row=4, column=1, padx=10, pady=10)
txta_comentario.grid(row=5, column=1, padx=10, pady=10)
scroll_vertical.grid(row=5, column=2, sticky="nsew")

txta_comentario.config(yscrollcommand=scroll_vertical.set)
txt_contrasena.config(show='*')

# CREACION DE LAS ETIQUETAS DE LOS CAMPOS DEL USUARIO: ---------------------------------------
lbl_id = Label(frame_usuario, text="Id:")
lbl_nombre = Label(frame_usuario, text="Nombre:")
lbl_contrasena = Label(frame_usuario, text="Contraseña:")
lbl_apellido = Label(frame_usuario, text="Apellido:")
lbl_direccion = Label(frame_usuario, text="Dirección:")
lbl_comentario = Label(frame_usuario, text="Comentario:")

lbl_id.grid(row=0, column=0,sticky="e" ,padx=10, pady=10)
lbl_nombre.grid(row=1, column=0,sticky="e" ,padx=10, pady=10)
lbl_contrasena.grid(row=2, column=0,sticky="e" ,padx=10, pady=10)
lbl_apellido.grid(row=3, column=0,sticky="e" ,padx=10, pady=10)
lbl_direccion.grid(row=4, column=0,sticky="e" ,padx=10, pady=10)
lbl_comentario.grid(row=5, column=0,sticky="e" ,padx=10, pady=10)

# CREACION DE BOTONES: ---------------------------------------
frame_btns = Frame(root)
frame_btns.pack()

btn_crear = Button(frame_btns, text="Create", command=crear_usuario)
btn_leer= Button(frame_btns, text="Read", command=get_usuario)
btn_actualizar = Button(frame_btns, text="Update", command=actualizar_usuario)
btn_eliminar = Button(frame_btns, text="Delete", command=eliminar_usuario)

btn_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)
btn_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)
btn_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)
btn_eliminar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
