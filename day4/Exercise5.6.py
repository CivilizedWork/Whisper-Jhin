import turtle
def koch(t,length):
    t=turtle.Turtle()
    if length<3:
        t.fd(length)
        return
    else :
        koch(t,length/3)
        t.lt(60)
        koch(t,length/3)
        t.rt(120)
        koch(t,length/3)
        t.lt(60)
        koch(t,length/3)
        turtle.mainloop()

def snowflake(t,length):
    for i in range(3):
        koch(t,length)
        t.rt(t,120)
bob=turtle.Turtle
bob.delay = 0

bob.x = -150
bob.y = 90

snowflake(bob, 300)

turtle.mainloop()