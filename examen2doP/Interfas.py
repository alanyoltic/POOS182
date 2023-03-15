from tkinter import  Tk, Button , Frame , Entry , Label
from datos import *

ventana = Tk()
ventana.title("MATRICULA")
ventana.geometry("400x400")


seccion1 = Frame(ventana,bg="brown")
seccion1.pack(expand=True,fill='both')



def trabajo():
    aux = generar(nombre.get())


#cabecera
txt1 = Label(seccion1,text="Usuario",bg="black",fg="white")
txt1.place(x=0, y=0)



#nombre
txt2 = Label(seccion1,text="Ingrese nombre",bg="black",fg="white")
txt2.place(x=0, y=40)

nombre = Entry
nombre.place(x=0,y=0)





txt1 = Label(seccion1,text="Ingrese apellido paterno",bg="black",fg="white")
txt1.place(x=0, y=80)





txt1 = Label(seccion1,text="Ingrese apellido materno",bg="black",fg="white")
txt1.place(x=0, y=120)

txt1 = Label(seccion1,text="Ingrese año de nacimiento",bg="black",fg="white")
txt1.place(x=0, y=160)

txt1 = Label(seccion1,text="Ingrese año de carrera",bg="black",fg="white")
txt1.place(x=0, y=200)
































ventana.mainloop()