from tkinter import messagebox, Tk, Button , Frame , Entry , Label 

ventana = Tk()
ventana.title("AUTOBUS")
ventana.geometry("300x400")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')



bustexto = Label(fondo,text="AUTOBUS",bg="blue",fg="white")
bustexto.place(x=0, y=0)








bustexto = Label(fondo,text="Marca",bg="white",fg="black")
bustexto.place(x=0, y=50)
paradas = Entry(width="30")
paradas.place(x=100, y=50)

bustexto = Label(fondo,text="Modelo",bg="white",fg="black")
bustexto.place(x=0, y=100)
paradas = Entry(width="30")
paradas.place(x=100, y=100)

bustexto = Label(fondo,text="Matricula",bg="white",fg="black")
bustexto.place(x=0, y=150)
paradas = Entry(width="30")
paradas.place(x=100, y=150)


bustexto = Label(fondo,text="N de asientos",bg="white",fg="black")
bustexto.place(x=0, y=200)
paradas = Entry(width="30")
paradas.place(x=100, y=200)

bustexto = Label(fondo,text="capasidad de tanque",bg="white",fg="black")
bustexto.place(x=0, y=250)
paradas = Entry(width="20")
paradas.place(x=130, y=250)






btnatasigdato= Button(fondo,text="Asignar ruta",fg="black",bg="white")
btnatasigdato.place(x=100,y=300,width=100,height=30)

btnatreporte= Button(fondo,text="Generar reporte",fg="black",bg="white")
btnatreporte.place(x=100,y=340,width=100,height=30)















ventana.mainloop()
