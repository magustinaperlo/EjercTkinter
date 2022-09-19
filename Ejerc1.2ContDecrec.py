
from tkinter import *
import tkinter.font as tkFont


def restar():
    valor=int(lineEdit["text"])
    lineEdit["text"]= f"{valor-1}"

ventana = Tk() 
ventana.title("Cont. Decreciente")
ventana.geometry('300x100')
ventana.config(bg="#FFF38C")
ventana.resizable(width=0, height=0)
fontEjemplo = tkFont.Font(family="Cambria", size=16, weight="bold", slant="roman")


etiqContador= Label (ventana, width=7, text= "Contador",bg="#C0B236",borderwidth=8)
etiqContador.place(x=0,y=0)
etiqContador.configure(font=fontEjemplo)

lineEdit= Label( ventana, text="88", width=7, bg= "#D9CB50",borderwidth=8)
lineEdit.place(x=100,y=0)
lineEdit.configure(font=fontEjemplo)


botonRestar= Button( ventana, width=6, text= "-",command= restar,borderwidth=4,bg="#F0E161")
botonRestar.place(x=210,y=0)
botonRestar.configure(font=fontEjemplo)

ventana.mainloop()