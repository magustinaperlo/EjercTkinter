
from tkinter import *
import tkinter.font as tkFont


def incrementar():
    valor=int(lineEdit["text"])
    lineEdit["text"]= f"{valor+1}"


ventana = Tk() 
ventana.title("Cont. Creciente")
ventana.geometry('300x100')
ventana.config(bg="#FFE3E1")
ventana.resizable(width=0, height=0)
fontEjemplo = tkFont.Font(family="Cambria", size=16, weight="bold", slant="roman")

etiqContador= Label (ventana, width=7, text="Contador",borderwidth=8, bg="#FFD1D1")
etiqContador.place(x=0,y=0)
etiqContador.configure(font=fontEjemplo)

lineEdit= Label( ventana, text="0", width=7, bg="#FF9494",borderwidth=8)
lineEdit.place(x=100,y=0)
lineEdit.configure(font=fontEjemplo)

botonIncrementar= Button( ventana, width=6, text="+", command= incrementar,borderwidth=4,bg="#FFF5E4")
botonIncrementar.place(x=210,y=0)
botonIncrementar.configure(font=fontEjemplo)

ventana.mainloop()