from tkinter import *
import tkinter.font as tkFont


def AñadirPeliculas():
    ListaPelic.insert(END, nombrePeli.get())
    nombrePeli.delete(0,END)

    

ventana= Tk()
ventana.geometry('500x300')
ventana.resizable(width=0, height=0)
ventana.title("Peliculas")
ventana.config(bg="#CED89E")

fontEjemplo = tkFont.Font(family="arial", size=10, weight="bold", slant="roman")
EtiquetaTitulo=Label(ventana,text="Escribe el título de una pelicula",bg="#9EB23B",borderwidth=6)
EtiquetaTitulo.place(x=20, y=20)
EtiquetaTitulo.configure(font=fontEjemplo)
EtiquetaPelicula=Label(ventana, text="Peliculas",bg="#9EB23B",borderwidth=5,width=20)
EtiquetaPelicula.place(x=300,y=20)
EtiquetaPelicula.configure(font=fontEjemplo)

nombrePeli = Entry(ventana,bg="#E0DECA",borderwidth=7,width=28)
nombrePeli.place(x=20, y=90)
nombrePeli.configure(font=fontEjemplo)

botonAñadir=Button(ventana, text="Añadir", command=AñadirPeliculas,borderwidth=5,fg="#4B8673")
botonAñadir.place(x=90, y=150)
botonAñadir.configure(font=fontEjemplo)

ListaPelic=Listbox(ventana, borderwidth=6,width=22,bg="#C7D36F")
ListaPelic.place(x=300,y=80)
ListaPelic.configure(font=fontEjemplo)


ventana.mainloop()