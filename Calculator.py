from tkinter import *

obj1 = Tk()
obj1.title("Calculator")
obj1.minsize(350,400)

equation = ""
def click(value):
    global equation
    equation = equation + str(value)
    answer.set(equation)

def calculate():
    global equation
    result = str(eval(equation))
    answer.set(result)  
    equation=""
    
def clear():
    global equation
    equation=""
    answer.set("")

answer = StringVar()
expression = Entry(obj1, textvariable = answer ,font = ('Helvetica',15))
expression.grid(columnspan = 4, ipadx = 55, ipady=30)

OpenBracket = Button(obj1,text = "(",height = 3,width = 6,command = lambda: click("("),font = ('Helvetica',15),borderwidth = 10)
OpenBracket.grid(row = 1,column = 0)

CloseBracket = Button(obj1,text = ")",height = 3,width = 6,command = lambda: click(")"),font = ('Helvetica',15),borderwidth = 10)
CloseBracket.grid(row = 1,column = 1)

modulo = Button(obj1,text = "%",height = 3,width = 6,command = lambda: click("%"),font = ('Helvetica',15),borderwidth = 10)
modulo.grid(row = 1,column = 2)

divide = Button(obj1,text = "/",height = 3,width = 6,command = lambda: click("/"),font = ('Helvetica',15),borderwidth = 10)
divide.grid(row = 1,column = 3)

button1 = Button(obj1,text = "1",height = 3,width = 6,command = lambda: click(1),font = ('Helvetica',15),borderwidth = 10)
button1.grid(row = 2,column = 0)

button3 = Button(obj1,text = "2",height = 3,width = 6,command = lambda: click(2),font = ('Helvetica',15),borderwidth = 10)
button3.grid(row = 2,column = 1)

button3 = Button(obj1,text = "3",height = 3,width = 6,command = lambda: click(3),font = ('Helvetica',15),borderwidth = 10)
button3.grid(row = 2,column = 2)

multiply = Button(obj1,text = "X",height = 3,width = 6,command = lambda: click("*"),font = ('Helvetica',15),borderwidth = 10)
multiply.grid(row = 2,column = 3)

button4 = Button(obj1,text = "4",height = 3,width = 6,command = lambda: click(4),font = ('Helvetica',15),borderwidth = 10)
button4.grid(row = 3,column = 0)

button6 = Button(obj1,text = "5",height = 3,width = 6,command = lambda: click(5),font = ('Helvetica',15),borderwidth = 10)
button6.grid(row = 3,column = 1)

button6 = Button(obj1,text = "6",height = 3,width = 6,command = lambda: click(6),font = ('Helvetica',15),borderwidth = 10)
button6.grid(row = 3,column = 2)

minus = Button(obj1,text = "-",height = 3,width = 6,command = lambda: click("-"),font = ('Helvetica',15),borderwidth = 10)
minus.grid(row = 3,column = 3)

button7 = Button(obj1,text = "7",height = 3,width = 6,command = lambda: click(7),font = ('Helvetica',15),borderwidth = 10)
button7.grid(row = 4,column = 0)

button8 = Button(obj1,text = "8",height = 3,width = 6,command = lambda: click(8),font = ('Helvetica',15),borderwidth = 10)
button8.grid(row = 4,column = 1)

button9 = Button(obj1,text = "9",height = 3,width = 6,command = lambda: click(9),font = ('Helvetica',15),borderwidth = 10)
button9.grid(row = 4,column = 2)

plus = Button(obj1,text = "+",height = 3,width = 6,command = lambda: click("+"),font = ('Helvetica',15),borderwidth = 10)
plus.grid(row = 4,column = 3)

buttonC = Button(obj1,text = "C",height = 3,width = 6,command = clear,font = ('Helvetica',15),borderwidth = 10)
buttonC.grid(row = 5,column = 0)

button0 = Button(obj1,text = "0",height = 3,width = 6,command = lambda: click(0),font = ('Helvetica',15),borderwidth = 10)
button0.grid(row = 5,column = 1)

dot = Button(obj1,text = ".",height = 3,width = 6,command = lambda: click("."),font = ('Helvetica',15),borderwidth = 10)
dot.grid(row = 5,column = 2)

equalsto = Button(obj1,text = "=",height = 3,width = 6,command = calculate,font = ('Helvetica',15),borderwidth = 10)
equalsto.grid(row = 5,column = 3)



obj1.configure(bg='black')
obj1.mainloop()
