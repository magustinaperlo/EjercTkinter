from tkinter import*
import tkinter.font as tkFont

def Calcular():
	n1 = num1.get()
	n2 = num2.get()
	op = opcion.get()
	if op==1:
		res.set(n1+n2)
	elif op==2:
		res.set(n1-n2)
	elif op==3:
		res.set(n1*n2)
	elif op==4:
		res.set(n1/n2)

	    
ventana=Tk()
ventana.title("Calculadora 2")
ventana.geometry('550x450')
ventana.resizable(width=0, height=0)
ventana.config(bg="#F5E8C7")

num1= DoubleVar()
num2= DoubleVar()
res = DoubleVar()
opcion = IntVar()


valor1=Label(ventana, text="Valor 1", bg="#F5E8C7",borderwidth=5)
valor1.place(x=30,y=100)
valor2=Label(ventana, text="Valor 2", bg="#F5E8C7",borderwidth=5)
valor2.place(x=30,y=160)
resultado=Label(ventana, text="Resultado", bg="#F5E8C7", borderwidth=5)
resultado.place(x=30,y=220)
Operaciones=Label(ventana, text="Operaciones", bg="#F5E8C7",borderwidth=5)
Operaciones.place(x=330,y=40)
fontEjemplo = tkFont.Font(family="Cambria", size=16, weight="bold", slant="roman")
valor1.configure(font=fontEjemplo)
valor2.configure(font=fontEjemplo)
resultado.configure(font=fontEjemplo)
Operaciones.configure(font=fontEjemplo)


EntValor1=Entry(ventana, bg="#DEB6AB",borderwidth=6, width=13,textvariable=num1)
EntValor1.place(x=150,y=100)
EntValor1.configure(font=fontEjemplo)

EntValor2=Entry(ventana, bg="#DEB6AB",borderwidth=6, width=13,textvariable=num2)
EntValor2.place(x=150,y=160)
EntValor2.configure(font=fontEjemplo)

LabelResultado=Label(ventana, bg="#ECCCB2",textvariable=res, borderwidth=5, width=13)
LabelResultado.place(x=150,y=220)
LabelResultado.configure(font=fontEjemplo)

#RadioButton

rboton1 = Radiobutton(ventana,text="Suma",value=1,variable=opcion,bg="#DEB6AB")
rboton1.place(x=340,y=100)
rboton2 = Radiobutton(ventana,text="Resta",value=2,variable=opcion,bg="#DEB6AB")
rboton2.place(x=340,y=140)
rboton3 = Radiobutton(ventana,text="Multiplicación",value=3,variable=opcion,bg="#DEB6AB")
rboton3.place(x=340,y=180)
rboton4 = Radiobutton(ventana,text="División",value=4,variable=opcion,bg="#DEB6AB")
rboton4.place(x=340,y=220)
rboton1.configure(font=fontEjemplo)
rboton2.configure(font=fontEjemplo)
rboton3.configure(font=fontEjemplo)
rboton4.configure(font=fontEjemplo)

#Boton
BotonCalcular=Button(ventana,text="Calcular",command=Calcular,borderwidth=5,bg="#AC7088")
BotonCalcular.place(x=150,y=300)
BotonCalcular.configure(font=fontEjemplo)







ventana.mainloop()