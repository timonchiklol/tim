from turtle import *
from function import *
from tkinter import *
speed(100000000000)
shape("turtle")


def click():
    command = txt.get()
    if command == "4":
        kvadrat()
    if command == "6":
        shesti()
    if command == "76":
        snow()
    if command == "b":
        color("black")
    if command == "y":
        color("yellow")
    if command == "r":
        color("red")
    if command == "b":
        color("blue")
def t():
    begin_fill()
    color("white")
    penup()
    setposition(-500,500)
    pendown()
    forward(1000)
    right(90)
    forward(1000)
    right(90)
    forward(1000)
    right(90)
    forward(1000)
    right(90)
    end_fill()
    setposition(0,0)
    color("black")

def g():
    clear()


window = Tk()
window.title(" yes but no")
window.geometry("400x50")
txt = Entry(window,width=30)
txt.grid(column=1,row=0)
btn=Button(window,text="da",command=click)
btn.grid(column=2,row=0)
btn5=Button(window,text="net",command=g)
btn5.grid(column=3,row=0)


window.mainloop()