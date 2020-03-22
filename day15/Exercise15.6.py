import math
import turtle
def polygon(t,n,length):
    t= turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(300/n)

class Circle:
    """
    attribute:center, radius.
    """
Circ = Circle()
Circ.radius = 10
def draw_circle(t, Circ):
    circumference = 2 * math.pi * Circ.radius
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

t = turtle.Turtle()
draw_circle(t, Circ)