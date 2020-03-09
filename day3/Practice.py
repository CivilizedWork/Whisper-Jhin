import math
import turtle
def polygne_1(t,n,length):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(200/ n)

def polygon(t,n,length):
    t= turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(300/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
polygne_1('job',10,40)
polygon('bob',50,20)
circle('bob',30)
turtle.mainloop()