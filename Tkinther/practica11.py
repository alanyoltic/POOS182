from tkinter import *

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
botonazul= Button(seccion1,text="boton azul",fg="blue")
botonazul.place(x=60,y=60,width=100,height=40)

botonnegro= Button(seccion2,bg="black",text="boton negro",fg="white")
botonnegro.grid(row=0,column=0)

botonamarillo= Button(seccion2,bg="yellow",text="boton amarillo",fg="black")
botonamarillo.grid(row=5,column=1)

botonverde= Button(seccion3,bg="green",text="boton verde",fg="white")
botonverde.pack()






ventana.mainloop()