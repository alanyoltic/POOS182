from tkinter import  Tk, Button , Frame , Entry , Label
import tkinter as Tk
from validador import *

aux=validar

def validarc():
    aux= validarc(usuario.get(),contra.get())


ventana = Tk()
ventana.title("BIENVENIDO")
ventana.geometry("800x600")


seccion1 = Frame(ventana,bg="purple")
seccion1.pack(expand=True,fill='both')
usuario= Tk.StringVar

contra = Entry(show="*", width="30")
contra.place(x=300, y=300)


contra= Tk.StringVar
usuario = Entry(width="30")
usuario.place(x=300, y=250)



botoningresar= Button(seccion1,text="Ingresar",fg="black", command=validarc)
botoningresar.place(x=300,y=350,width=80,height=30)
botoncancelar= Button(seccion1,text="cancelar",fg="black")
botoncancelar.place(x=400,y=350,width=80,height=30)









usu = Label(seccion1,text="Usuario")
usu.place(x=300, y=230)

conta = Label(seccion1,text="Contraseña")
conta.place(x=300, y=280)









ventana.mainloop()