from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")
root.geometry("+500+80")


mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)


entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1)
Label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
Label_entrada2 =ttk.Label(mainframe, textvariable=entrada2)
Label_entrada1.grid(column=0, row=1, columnspan=4, sticky=(W, E))

Button0 = ttk.Button(mainframe, text="0")
Button1 = ttk.Button(mainframe, text="1")
Button2 = ttk.Button(mainframe, text="2")
Button3 = ttk.Button(mainframe, text="3")
Button4 = ttk.Button(mainframe, text="4")
Button5 = ttk.Button(mainframe, text="5")
Button6 = ttk.Button(mainframe, text="6")
Button7 = ttk.Button(mainframe, text="7")
Button8 = ttk.Button(mainframe, text="8")
Button9 = ttk.Button(mainframe, text="9")

Button_borrar = ttk.Button(mainframe, text=chr(9003))
Button_borrar_todo = ttk.Button(mainframe, text="C")
Button_borrar_parentesis1 = ttk.Button(mainframe, text="(")
Button_borrar_parentesis2 = ttk.Button(mainframe, text=")")
Button_punto = ttk.Button(mainframe, text=".")


Button_division = ttk.Button(mainframe, text=chr(247))
Button_multiplicacion = ttk.Button(mainframe, text="X")
Button_resta = ttk.Button(mainframe, text="-")
Button_suma = ttk.Button(mainframe, text="+")

Button_igual= ttk.Button(mainframe, text="=")
Button_raiz_cuadrada = ttk.Button(mainframe, text="√")

Button_borrar_parentesis1.grid(column=0, row=2)
Button_borrar_parentesis2.grid(column=1, row=2)
Button_borrar_todo.grid(column=2, row=2)
Button_borrar.grid(column=3, row=2)

Button7.grid(column=0, row=3)
Button8.grid(column=1, row=3)
Button9.grid(column=2, row=3)
Button_division.grid(column=3, row=3)

Button4.grid(column=0, row=4)
Button5.grid(column=1, row=4)
Button6.grid(column=2, row=4)
Button_multiplicacion.grid(column=3, row=4)

Button1.grid(column=0, row=5)
Button2.grid(column=1, row=5)
Button3.grid(column=2, row=5)
Button_suma.grid(column=3, row=5)


Button0.grid(column=0, row=6, columnspan=2, sticky=(W,E))
Button_punto.grid(column=2, row=6)
Button_resta.grid(column=3, row=6)

Button_igual.grid(column=0, row=7, columnspan=3, sticky=(W,E))
Button_raiz_cuadrada.grid(column=3, row=7)

root,mainloop()