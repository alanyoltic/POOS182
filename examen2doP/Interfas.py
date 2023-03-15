import tkinter as Tk
from tkinter import  Tk, Button , Frame , Entry , Label




def generar():
    aux = generar(nombre.get(),apellidoP.get(),apellidoM.get(),añoN.get(),añoC.get())

ventana = Tk()
ventana.title("MATRICULA")
ventana.geometry("400x400")


seccion1 = Frame(ventana,bg="brown")
seccion1.pack(expand=True,fill='both')






#cabecera
txt1 = Label(seccion1,text="Usuario",bg="black",fg="white")
txt1.place(x=0, y=0)



#nombre
txt2 = Label(seccion1,text="Ingrese nombre",bg="black",fg="white")
txt2.place(x=0, y=40)

nombre = Tk
nombre = Entry(width="20")
nombre.place(x=0,y=0)





txt1 = Label(seccion1,text="Ingrese apellido paterno",bg="black",fg="white")
txt1.place(x=0, y=80)

apellidoP = Tk
apellidoP = Entry
apellidoP.place(x=0,y=0)




txt1 = Label(seccion1,text="Ingrese apellido materno",bg="black",fg="white")
txt1.place(x=0, y=120)


apellidoM = Tk
apellidoM = Entry(width="20")
apellidoM.place(x=0,y=0)

txt1 = Label(seccion1,text="Ingrese año de nacimiento",bg="black",fg="white")
txt1.place(x=0, y=160)

añoN = Tk
añoN = Entry(width="20")
añoN.place(x=0,y=0)

txt1 = Label(seccion1,text="Ingrese año de carrera",bg="black",fg="white")
txt1.place(x=0, y=200)


añoC = Tk
añoC = Entry(width="20")
añoC.place(x=0,y=0)

botoningresar= Button(seccion1,text="GENERAR",fg="black", command=generar)
botoningresar.place(x=300,y=350,width=80,height=30)






























ventana.mainloop()