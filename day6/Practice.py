x=5
print(x)
x=7
print(x)
a=5
b=a
a=3
print(b)
x=0
x=x+1
def countdown(n):
    while n>0:
        print(n)
        n=n-1
    print('Blastoff!')

def sequence(n):
    while n!=1:
        print(n)
        if n%2==0:
            n=n/2
        else:
            n=n*3+1

def print_n(n):
    if n>1:
        print(n)
        n=n-1
        return print_n(n)
    else:
        print(1)

def print_n(n):
    while n!=1:
        print(n)
        n=n-1
    print(1)

print_n(23)
while True:
    line = input ('>')
    if line=='done':
        break
    print(line)

print('Done!')
while True:
    print(x)
    y=(x+a/x)/2
    if y==x:
        break
    x=y
    if abs(y - x) < 0.00001:
        break

