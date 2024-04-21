# En python, el primer elemento de gui es una ventana denominada raiz.
# por convencion a la ventana se la denomina: raiz.
# para agregar un icono es necesario tener una imagen con extenciuon.ico, buscar conversor .ico en google
# si cambiamos la extencion del archivo por .pyw abrira directamente la ventana al darle doble click.
# En python todo elemento grafico es un widget
from tkinter import *

raiz = Tk()

raiz.title('Ventana de Pruebas')
raiz.resizable(True, True)#redimension en ancho, alto
#raiz.geometry("650x350") --> siempre se va a adaptar a su contenido.
raiz.config(bg="gray")

frame = Frame()
frame.pack(fill="both", expand="True")# empaqueta el frame dentro de la raiz.
frame.config(width="650", height="350", bg="red")
raiz.mainloop()