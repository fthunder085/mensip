import turtle
from time import *


t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(140)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-65,130)
t.pendown()
t.color('white')
t.write(" Love You", font=("Verdana",25,"bold"))

t.penup()
t.goto(-75,-130)
t.pendown()
t.color('white')
t.write("Bin Hyung", font=("Verdana",25,"bold"))

sleep(10)