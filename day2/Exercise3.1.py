def right_justify(s):
    print(' '*(70-len('s'))+s)

right_justify('monty')
def do_twice(f,g):
    f(g)
    f(g)

def print_spam(t):
    print('t')

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice,'spam')
def do_four(f,g):
    do_twice(f,g)
    do_twice(f,g)

do_four(print_spam(),'spam')
