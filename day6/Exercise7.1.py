import math
def mysqrt(a):
    x=a*3/4
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return y
def test_squre_root():
    print('a'+' '+'mysqrt(a)'+' '+'math.sqrt(a)'+' '+'diff')
    print('-'+' '+'---------'+' '+'------------'+' '+'----')
    t=1
    while t<10:
        print(t,' ',round(mysqrt(t),13),' ',round(math.sqrt(t),13),' ',round(abs(mysqrt(t)-math.sqrt(t)),13))
        t=t+1
test_squre_root()