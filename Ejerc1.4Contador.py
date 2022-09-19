from tkinter import *
import tkinter.font as tkFont

def decrementar():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=f"{valor-1}"

def incrementar():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=f"{valor+1}"

def reset():
    valor=int(etiquetaValor["text"])
    etiquetaValor["text"]=0

ventana=Tk()
ventana.title("Contador")
ventana.geometry('470x100')
ventana.config(bg="#F7ECDE")
ventana.resizable(width=0, height=0)

fontEjemplo = tkFont.Font(family="Cambria", size=16, weight="bold", slant="roman")
etiquetaCont=Label(ventana, text="Contador=",bg="#E9DAC1",borderwidth=8,width=8)
etiquetaCont.place(x=0,y=0)
etiquetaCont.configure(font=fontEjemplo)
etiquetaValor=Label(ventana,text="0",bg="#F7ECDE",borderwidth=8,width=5)
etiquetaValor.place(x=110,y=0)
etiquetaValor.configure(font=fontEjemplo)

botonDecrem=Button(ventana,text="DOWN -",command=decrementar,bg="#54BAB9",borderwidth=6,width=6)
botonDecrem.place(x=180,y=0)
botonDecrem.configure(font=fontEjemplo)

botonIncrem=Button(ventana,text="UP +",command=incrementar,bg="#9ED2C6",borderwidth=6,width=6)
botonIncrem.place(x=275,y=0)
botonIncrem.configure(font=fontEjemplo)

botonReset=Button(ventana,text="RESET",command=reset,bg="#E9DAC1",borderwidth=6,width=6)
botonReset.place(x=370,y=0)
botonReset.configure(font=fontEjemplo)


ventana.mainloop()