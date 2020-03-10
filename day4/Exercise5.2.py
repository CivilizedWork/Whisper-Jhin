def check_fermat(a,b,c,n):
    if n>2 and a**n+b**n==c**n:
        print('Holy smokes,Fermat was wrong')
    else:
        print('No,that doesn\'t work')

def caution_input():
    a=input('请输入a的值')
    b=input('请输入b的值')
    c=input('请输入c的值')
    n=input('请输入n的值')
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    check_fermat(a,b,c,n)

caution_input()

