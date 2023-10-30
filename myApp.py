from tkinter import *

Raiz = Tk()

myFrame = Frame(Raiz, width=500, height=800)
myFrame.config(bg="grey")
myFrame.pack()

operacion = ""
resultado = 0
#----------------------------------------------------

numeropanel = StringVar()




panel = Entry(myFrame, textvariable=numeropanel)
panel.grid(row=0, column=0, pady=10, padx=10, columnspan=4)
panel.config(bg="#A0AEA9", fg="black")

#----------------------------------------------------

def numero(num):
    global operacion
    
    if operacion != "":
        numeropanel.set(num)
        operacion=""
    else:
        numeropanel.set(numeropanel.get() + f"{num}")
#----------------------------------------------------

def suma(num):
    global operacion
    global resultado
    
    resultado += int(num)
    operacion = "suma"
    
    numeropanel.set(resultado)
    #----------------------------------------------------

def resta(num):
    global operacion
    global resultado
    
    resultado -= int(num)
    operacion = "resta"
    
    numeropanel.set(resultado)
#----------------------------------------------------

def multiplicacion(num):
    global operacion
    global resultado
    
    resultado = resultado * int(num)
    operacion = "multiplicacion"
    
    numeropanel.set(resultado)
#----------------------------------------------------

def division(num):
    global operacion
    global resultado
    
    resultado /= int(num)
    operacion = "division"
    
    numeropanel.set(resultado)
#----------------------------------------------------

def resultadototal():
    global resultado
    
    numeropanel.set(resultado + int(numeropanel.get()))
    
    resultado = 0

#----------------------------------------------------

boton7 = Button(myFrame, text="7", width=3, command=lambda:numero(7))
boton7.grid(row=1, column=0)
boton8 = Button(myFrame, text="8", width=3, command=lambda:numero(8))
boton8.grid(row=1, column=1)
boton9 = Button(myFrame, text="9", width=3, command=lambda:numero(9))
boton9.grid(row=1, column=2)


boton_suma = Button(myFrame, text="+", width=3, command=lambda:suma(numeropanel.get()))
boton_suma.grid(row=1, column=3)


#----------------------------------------------------
boton_resta = Button(myFrame, text="-", width=3, command=lambda:resta(numeropanel.get()))
boton_resta.grid(row=2, column=3)

boton4 = Button(myFrame, text="4", width=3, command=lambda:numero(4))
boton4.grid(row=2, column=0)
boton5 = Button(myFrame, text="5", width=3, command=lambda:numero(5))
boton5.grid(row=2, column=1)
boton6 = Button(myFrame, text="6", width=3, command=lambda:numero(6))
boton6.grid(row=2, column=2)


#----------------------------------------------------
boton_multiplicacion = Button(myFrame, text="*", width=3, command=lambda:multiplicacion(numeropanel.get()))
boton_multiplicacion.grid(row=3, column=3)

boton1 = Button(myFrame, text="1", width=3, command=lambda:numero(1))
boton1.grid(row=3, column=0)
boton2 = Button(myFrame, text="2", width=3, command=lambda:numero(2))
boton2.grid(row=3, column=1)
boton3 = Button(myFrame, text="3", width=3, command=lambda:numero(3))
boton3.grid(row=3, column=2)


#----------------------------------------------------
boton_division = Button(myFrame, text="/", width=3, command=lambda:division(numeropanel.get()))
boton_division.grid(row=4, column=3)

botonpotencia = Button(myFrame, text="**", width=3)
botonpotencia.grid(row=4, column=0)
boton0 = Button(myFrame, text="0", width=3)
boton0.grid(row=4, column=1)
botonIgual = Button(myFrame, text="=", width=3, command=lambda:resultadototal())
botonIgual.grid(row=4, column=2)


Raiz.mainloop()