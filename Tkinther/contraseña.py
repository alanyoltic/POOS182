from tkinter import  Tk, Button , Frame , Entry , Label
from validador import *



ventana = Tk()
ventana.title("BIENVENIDO")
ventana.geometry("500x500")


seccion1 = Frame(ventana,bg="purple")
seccion1.pack(expand=True,fill='both')


inicio= Label(seccion1,text="Generador de contraseñas")
inicio.place(x=200,y=0)







ventana.mainloop()
