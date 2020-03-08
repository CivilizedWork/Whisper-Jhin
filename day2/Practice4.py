def square(t,length):
    import turtle
    t= turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)

    turtle.mainloop()

#square('bob',500)
def polygon(t,length,n):
    import turtle
    t= turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

    turtle.mainloop()

#polygon('bob',100,6)
import math
def circle(t,r):
    import turtle
    t= turtle.Turtle()
    n=50
    for i in range(n):
        t.fd(2*math.pi*r/n)
        t.lt(360/n)

    turtle.mainloop()

#circle('bob',30,50)
def arc(t,r,angle):
    import turtle
    t= turtle.Turtle()
    n=50
    for i in range(n):
        t.fd(2*math.pi*r/n)
        t.lt(angle/n)

    turtle.mainloop()

#arc('bob',30,50,180)
def circle(t,r,n):
    arc(t,r,n,360)

circle('bob',30,50)