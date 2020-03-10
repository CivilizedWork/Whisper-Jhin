minutes=105
print(minutes/60)
hours=minutes//60
print(hours)
remainder=minutes-hours*60
print(remainder)
remainder=minutes%60
print(remainder)
print(5==5)
print(5==6)
print(type(True),type(False))
"""x!=y
x>y
x<y
x>=y
x<=y
"""
print(42 and True)
"""
if x>0:
    print('x is positive')
if x<0:
    pass
if x%2==0:
    print('x is even')
else:
    print('x is odd')
if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else :
    print('x and y and equal')
if choice =='a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()
if x == y:
    print('x and y are equal')
else:
    if x<y:
         print('x is less than y')
    else :
         print('x is greater than y')
if 0<x:
    if x<10:
         print('x is x is a positive single-digit number'.)
if 0<x and x<10:
    print('x is a positive single-digit number.')
if 0<x<10:
    print('x is a positive single-digit number.')
"""
def countdown(n):
    if n<=0:
        print('Blastoff!')
    else :
        print(n)
        countdown(n-1)

countdown(3)
def print_n(s,n):
    if n<=0:
        return
    print(s)
    print_n(s,n-1)

def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)

def recurse():
    recurse()

#name= input ('What is your name?\n')
#print(name)
#prompt= 'What...is the airspeed velocity of an unladen swallow?\n'
#speed=input(prompt)
#print(speed)
x=5
y=6
import math
signal_power=9
noise_power=10
ratio = signal_power // noise_power
decibles=10*math.log10(ratio)
print(decibles)





