from tkinter import*
from random import*

def GenerarNumero():
    if int(numvariable1.get()) > int(numvariable2.get()):
        nroRan=str(randint(int(numvariable2.get()), int(numvariable1.get())))
        Numero.set(nroRan)
    elif int(numvariable1.get()) < int(numvariable2.get()):
        nroRan=str(randint(int(numvariable1.get()), int(numvariable2.get())))
        Numero.set(nroRan)

ventana=Tk()
ventana.title("Generador de números")
ventana.geometry('500x300')
#fijamos los valores para que el usuario no extienda ni achique demasiado la ventana.
ventana.minsize(500, 300) 
ventana.maxsize(500, 300)
ventana.config(bg="#BFACE0")

num1=Label(ventana, text="Número 1", bg="#A084CA",borderwidth=5,font="arial,14")
num1.place(x=80,y=50)
num2=Label(ventana, text="Número 2", bg="#A084CA",borderwidth=5,font="arial,14")
num2.place(x=80,y=120)

numvariable1=StringVar()
numvariable2=StringVar()

#se añade el estado en el Spinbox para que el usuario NO ingrese valores manualmente y utilice el spinbox
box1=Spinbox(ventana, from_=0,fg="#533483", to_= 5000, textvariable=numvariable1,borderwidth=10, state="readonly")
box1.place(x=270,y=50)
box2=Spinbox(ventana, from_=0,fg="#533483", to_= 5000, textvariable=numvariable2,borderwidth=10,state="readonly")
box2.place(x=270,y=120)

EtiqNumGener=Label(ventana, text="Numero Generado", bg="#645CAA",borderwidth=8,font="arial,12")
EtiqNumGener.place(x=80,y=170)

Numero= StringVar()
NumGenerado=Label(ventana, textvariable=Numero, width=18,borderwidth=10)
NumGenerado.place(x=270,y=170)

BotonGener=Button(ventana, text="Generar", command=GenerarNumero,fg="#533483",borderwidth=10)
BotonGener.place(x=270,y=230)

ventana.mainloop()
