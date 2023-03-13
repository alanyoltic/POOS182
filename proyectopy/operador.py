from tkinter import messagebox, Tk, Button , Frame , Entry , Label 

ventana = Tk()
ventana.title("OPERADOR")
ventana.geometry("300x400")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')



bustexto = Label(fondo,text="OPERADOR",bg="blue",fg="white")
bustexto.place(x=0, y=0)








bustexto = Label(fondo,text="Nombre",bg="white",fg="black")
bustexto.place(x=0, y=50)
paradas = Entry(width="30")
paradas.place(x=100, y=50)

bustexto = Label(fondo,text="Apellido paterno",bg="white",fg="black")
bustexto.place(x=0, y=100)
paradas = Entry(width="30")
paradas.place(x=100, y=100)

bustexto = Label(fondo,text="Apellido materno",bg="white",fg="black")
bustexto.place(x=0, y=150)
paradas = Entry(width="30")
paradas.place(x=100, y=150)


bustexto = Label(fondo,text="Numero de empleado",bg="white",fg="black")
bustexto.place(x=0, y=200)
paradas = Entry(width="30")
paradas.place(x=100, y=200)

bustexto = Label(fondo,text="Licencia",bg="white",fg="black")
bustexto.place(x=0, y=250)
paradas = Entry(width="30")
paradas.place(x=100, y=250)

bustexto = Label(fondo,text="vigencia",bg="white",fg="black")
bustexto.place(x=0, y=300)
paradas = Entry(width="30")
paradas.place(x=100, y=300)



btnatasigdato= Button(fondo,text="Insertar",fg="black",bg="white")
btnatasigdato.place(x=180,y=340,width=80,height=50)

btnatreporte= Button(fondo,text="Eliminar",fg="black",bg="white")
btnatreporte.place(x=30,y=340,width=80,height=50)















ventana.mainloop()
