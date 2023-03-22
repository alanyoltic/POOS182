from tkinter import *
from tkinter import ttk
import tkinter as tk 







ventana = Tk()
ventana.title 
ventana.geometry("500x500")


panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")


pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)


titulo = Label(pestaña1,text="registro de usuarios",fg="blue",font=("modern",18)).pack()



varNoe= tk.StringVar
ibiNoe= Label(pestaña1,text="nombre: ").pack()
txtNoe= Entry(pestaña1,textvariable=varNoe).pack()

varNoe2= tk.StringVar
ibiNoe2= Label(pestaña1,text="correo: ").pack()
txtNoe2= Entry(pestaña1,textvariable=varNoe2).pack()


varNoe3= tk.StringVar
ibiNoe3= Label(pestaña1,text="contraseña: ").pack()
txtNoe3= Entry(pestaña1,textvariable=varNoe3).pack()

btnguardar = Button(pestaña1,text="guardar").pack()


panel.add(pestaña1, text="formulario usuarios")
panel.add(pestaña2, text="buscar usuario")
panel.add(pestaña3, text="consutar usuario")
panel.add(pestaña4, text="xd")
ventana.mainloop()














