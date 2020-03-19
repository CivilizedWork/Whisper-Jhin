t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')
t1 = 'a',
print(type(t1))
t2 = ('a')
print(type(t2))
t = tuple()
print(t)
t = tuple('lupins')
print(t)
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])
#t[0] = 'A'
t = ('A',)+t[1:]
print(t)
print((0,1,2)<(0,3,4))
print((0,1,2000000)<(0,3,4))
a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)
a,b=b,a
print(a,b)
#a, b = 1, 2, 3
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)
t = divmod(7,3)
print(t)
quot, rem = divmod(7,3)
print(quot,rem)
def min_max(t):
    return min(t), max(t)

def printall(*args):
    print(args)

printall(1, 2.0, '3')
t = (7,3)
#divmod(t)
print(divmod(*t))
print(max(1,2,3))
#sum(1,2,3)
def small(*t):
    return sum(t)

print(small(1,2,3,5,6))
s = 'abc'
t = [0,1,2]
print(zip(s,t))
for pair in zip(s,t):
    print([pair])

print(list(zip(s,t)))
print(list(zip('Anne','Eik')))
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number,letter)
def has_match(t1,t2):
    for x ,y in zip(t1,t2):
        if x == y:
            return True
    return False

for index, element in enumerate('abc'):
    print(index,element)

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)
for key, value in d.items():
    print(key,value)

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)
d = dict(zip('abc',range(3)))
print(d)
"""
directory[last, first] = number
for last,first in directory:
    print(last,first,directory[last,first])
    
"""
from structshape import  structshape
t = [1,2,3]
structshape(t)
t2 = [[1,2], [3,4], [5,6]]
structshape(t2)
t3 = [1,2,3,4.0,'5','6',[7],[8],9]
structshape(t3)
s = 'abc'
lt = list(zip(t,s))
structshape(lt)
d = dict(lt)
structshape(d)
