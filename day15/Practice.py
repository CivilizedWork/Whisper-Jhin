import math
class Point:
    """Represents a point in 2-D space."""

print(Point)
blank = Point()
print(blank)
blank.x = 3.0
blank.y = 4.0
print(blank.y)
x = blank.x
print(x)
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)
def distance_between_points(p1,p2):
    distance= math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    return distance

print(distance_between_points(blank,blank))
class Rectangle:
    """
    Represents a rectangle.
    attributes: width, height, corner.
    """
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)
box.width = box.width + 50
box.height = box.height + 100
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width,box.height)

grow_rectangle(box, 50, 100)
print(box.width, box.height)
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

p1 = Point()
p1.x = 3.0
p1.y = 4.0
import copy
p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print(p1 is p2)
print(p1 == p2)
box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)
box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)
def move_rectangle_new(rect,dx,dy):
    rect1 = copy.deepcopy(rect)
    rect1.corner.x += dx
    rect1.corner.y += dy

p = Point()
p.x = 3
p.y = 4
#print(p.z)
print(type(p))
print(isinstance(p,Point))
print(hasattr(p, 'x'))
print(hasattr(p, 'z'))
try:
    x = p.x
except AttributeError:
    x = 0

