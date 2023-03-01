from tkinter import messagebox, Tk, Button , Frame 

#5.- agregar funcion de mensaje.
def mostrarmen():
    messagebox.showinfo("informacion","te informo que todo fallo con exito" )
    messagebox.showerror("error","si te e fallado te pido perdon")
    print (messagebox.askokcancel("pregunta","seguro que quieres cerrar"))
    print (messagebox.askquestion("pregunta","seguro que quieres cerrar"))
    print (messagebox.askretrycancel("pregunta","seguro que quieres cerrar"))
    print (messagebox.askyesno("pregunta","seguro que quieres cerrar"))
    print (messagebox.askyesnocancel("pregunta","seguro que quieres cerrar"))
    


#6.- agregar botones
def agregarboton():
    botonverde.config(text="+", bg="#991a93",fg="#cf131c")
    botonuevo=Button(seccion3,text="boton nuevo")
    botonuevo.pack()





#1 generar una ventana
ventana = Tk()
ventana.title("ejemplo de 3")
ventana.geometry("600x400") 



#2 agregar frames
seccion1 = Frame(ventana,bg="purple")
seccion1.pack(expand=True,fill='both')

seccion2 = Frame(ventana,bg="yellow")
seccion2.pack(expand=True,fill='both')

seccion3 = Frame(ventana,bg="green")
seccion3.pack(expand=True,fill='both')


#3. agregar botones
botonazul= Button(seccion1,text="boton azul",fg="blue", command=mostrarmen,)
botonazul.place(x=60,y=60,width=100,height=40)







botonnegro= Button(seccion2,bg="black",text="boton negro",fg="white")
botonnegro.grid(row=0,column=0)

botonamarillo= Button(seccion2,bg="yellow",text="boton amarillo",fg="black")
botonamarillo.grid(row=5,column=1)

botonverde= Button(seccion3,bg="green",text="boton verde",fg="white", command=agregarboton)
botonverde.pack()






ventana.mainloop()