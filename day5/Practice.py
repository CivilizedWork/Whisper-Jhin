import math
#e=math.exp(1.0)
#height=radius*math.sin(radians)
def area(radius):
    a=math.pi*radius**2
    return a

def area(radius):
    return(math.pi*radius**2)

def absolute_value(x):
    if x<0:
        return -x
    else:
        return x

def absolute_value(x):
    if x<0:
        return -x
    if x>0:
        return x

def than_0(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    elif x==y:
        return 0

def distance(x1,y1,x2,y2):
    return 0.0

def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    print('dx is',dx)
    print('dy is',dy)
    return 0.0

#distance(1,2,4,6)
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    print('disquared is',dsquared)
    return 0.0

#distance(1,2,4,6)
def distance(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    dsquared = dx ** 2 + dy ** 2
    result=math.sqrt(dsquared)
    print(result)
    return result

#distance(1,2,4,6)
def hypotenuse(a,b):
    dsquared=a**2+b**2
    print('dsquared is ',dsquared)
    return 0.0

def hypotenuse(a,b):
    dsquared=a**2+b**2
    result=math.sqrt(dsquared)
    return result

def circle_area(xc,yc,xp,yp):
    radius=distance(xc,yc,xp,yp)
    result=area(radius)
    return result

def circle_area(xc,yc,xp,yp):
    return area(distance(xc,yc,xp,yp))

def is_divisible(x,y):
    if x%y==0:
        return True
    else:
        return False

print(is_divisible(6,4))
print(is_divisible(6,3))
def is_divisible(x,y):
    return x%y==0

# is_divisible(x,y):
#print('x is divisible by y')
#if is_divisible(x,y)==True:
#print('x is divisible by y')
def is_between(x,y,z):
    if x<=y<=z:
        return True
    else:
        return False

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    if not isinstance(n,int):
        print('factorial is only defined for integers')
        return None
    elif n<0:
        print('factorial is not defined for negative integers')
        return None
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

factorial('fred')
factorial(-2)
def factorial(n):
    space=' '*(4*n)
    print(space,'factorial',n)
    if n==0:
        print(space ,'returning 1')
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        print(space,'returning',result)
        return result

