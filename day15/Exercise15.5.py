import turtle
class Rectangle:
    """
    Represents a rectangle.
    attributes: width, height, corner.
    """

t = turtle.Turtle()
rect = Rectangle()
rect.width = 100
rect.height = 50
def draw_rect(t, rect):
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)

draw_rect(t,rect)