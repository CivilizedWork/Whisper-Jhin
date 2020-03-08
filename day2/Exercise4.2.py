import math
import turtle
def arc(t,r,angle):
    bob = turtle.Turtle()
    t= turtle.Turtle()
    n=50
    for i in range(n):
        t.fd(2*math.pi*r/n)
        t.lt(angle/n)

    turtle.mainloop()
def petal (t,r,angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

def move(t,length):
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()