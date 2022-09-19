
from tkinter import*
from tkinter import messagebox
import tkinter.font as tkFont



def sumar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.place()
     
        if valor1=="" or valor2=="":
            labelResultado["text"]="Faltan valores para hacer la operacion suma"
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) + int(valor2)
            labelResultado["text"]=resultado

    except:
        messagebox.showerror("Error", "Ingrese un numero, NO una letra")

def restar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.place()
     
        if valor1=="" or valor2=="":
            labelResultado["text"]="Faltan valores para hacer la operacion resta"
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) - int(valor2)
            labelResultado["text"]=resultado

    except:
        messagebox.showerror("Error", "Ingrese un numero, NO una letra") 

def multiplicar():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.place()
     
        if valor1=="" or valor2=="":
            labelResultado["text"]="Faltan valores para hacer la operacion multiplicación"
            messagebox.showwarning("Error", "Ingrese un valor correcto")
        else:
            resultado=int(valor1) * int(valor2)
            labelResultado["text"]=resultado

    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")

def dividir():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.place()
     
        if valor1=="" or valor2=="" or valor1==0 or valor2==0:
            labelResultado["text"]="Faltan valores para hacer la operacion división"
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) / int(valor2)
            labelResultado["text"]=resultado

    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")   

def porcentaje():
    try:
        valor1=eValor1.get()
        valor2=eValor2.get()
        labelResultado.place()
     
        if valor1=="" or valor2=="":
            labelResultado["text"]="Faltan valores para hacer obtener el porcentaje"
            messagebox.showwarning("Error", "Falta ingresar uno o mas valores")
        else:
            resultado=int(valor1) % int(valor2)
            labelResultado["text"]=resultado

    except:
        messagebox.showerror("Error", "Ingrese un valor correcto")  

def reset():
    valor=int(labelResultado["text"])
    labelResultado["text"]=0
    eValor1.delete(0, END)
    eValor2.delete(0, END)


ventana=Tk()
ventana.title("Calculadora")
ventana.geometry('305x250')
ventana.resizable(width=0, height=0)
ventana.config(bg="#FDD7AA")

fontEjemplo = tkFont.Font(family="arial", size=10, weight="bold", slant="roman")
labelValor1=Label(ventana, text="VALOR 1",width=17,borderwidth=8,bg="#FDD7AA")
labelValor1.place(x=0,y=0)
labelValor1.configure(font=fontEjemplo)
eValor1=Entry(ventana,borderwidth=7,width=18,bg="#B6FFCE")
eValor1.place(x=160,y=0)
eValor1.configure(font=fontEjemplo)
labelValor2=Label(ventana, text="VALOR 2",width=17,borderwidth=8,bg="#FDD7AA")
labelValor2.place(x=0,y=40)
labelValor2.configure(font=fontEjemplo)
eValor2=Entry(ventana,borderwidth=7,width=18,bg="#B6FFCE")
eValor2.place(x=160,y=40)
eValor2.configure(font=fontEjemplo)
Etiqueta3=Label(ventana, text="RESULTADO =",width=17,borderwidth=8,bg="#FDD7AA")
Etiqueta3.place(x=0,y=80)
Etiqueta3.configure(font=fontEjemplo)

labelResultado=Label(ventana, bg="#B6FFCE", width=15,borderwidth=8)
labelResultado.place(x=160,y=80)
labelResultado.configure(font=fontEjemplo)

#BOTONES
sumar=Button(ventana, text="+", command= sumar, width=17,bg="#FFA8A8",borderwidth=6)
sumar.place(x=0,y=120)
sumar.configure(font=fontEjemplo)
restar=Button(ventana, text="-", command=restar,bg="#FFA8A8",width=16,borderwidth=6)
restar.place(x=160,y=120)
restar.configure(font=fontEjemplo)
multiplicar=Button(ventana, text="*", command=multiplicar,bg="#FFA8A8",width=17,borderwidth=6)
multiplicar.place(x=0,y=160)
multiplicar.configure(font=fontEjemplo)
dividir=Button(ventana, text="/", command=dividir,bg="#FFA8A8",width=16,borderwidth=6)
dividir.place(x=160,y=160)
dividir.configure(font=fontEjemplo)
porcentaje=Button(ventana, text="%", command=porcentaje,bg="#FFA8A8",width=17,borderwidth=6)
porcentaje.place(x=0,y=200)
porcentaje.configure(font=fontEjemplo)
clear=Button(ventana, text="CLEAR", bg="#B6FFCE", command=reset,width=16,borderwidth=6)
clear.place(x=160,y=200)
clear.configure(font=fontEjemplo)

ventana.mainloop()