class Point:
    """
    Represents a point in 2-D space.
    """


class Circle:
    """
    attribute:center, radius.
    """


b = Point()
b.x = 3.0
b.y = 4.0
a = Circle()
a.center = Point
a.center.x = 150
a.center.y = 100
a.radius = 75
import math


def distance_between_points(p1, p2):
    distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distance


def point_in_circle(Circ, Poin):
    if distance_between_points(Circ.center, Poin) < Circ.radius:
        return True


point_in_circle(a, b)


class Rectangle:
    """
    Represents a rectangle.
    attributes: width, height, corner.
    """


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p


def rect_in_circle(Circ, rect):
    if distance_between_points(Circ.corner, find_center(rect)) < Circ.radius and distance_between_points(
            find_center(rect), Circ.center):
        return True


import copy


def rect_circle_overlap(Circ, rect):
    p = copy.copy(rect.corner)
    if distance_between_points(Circ.corner, p) >= Circ.radius:
        return False
    p.x += rect.width
    if distance_between_points(Circ.corner, p) >= Circ.radius:
        return False
    p.x -= rect.width
    if distance_between_points(Circ.corner, p) >= Circ.radius:
        return False
    p.y += rect.height
    if distance_between_points(Circ.corner, p) > Circ.radius:
        return False
    p.y -= rect.height
    if distance_between_points(Circ.corner, p) > Circ.radius:
        return False
    else:
        return True

