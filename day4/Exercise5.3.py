def is_triangle(a,b,c):
    if a+b<c and b+c<a and a+c<b:
        print('No')
    else:
        print('Yes')

def caution_input():
    a=input('请输入第一个整数：')
    b=input('请输入第二个整数：')
    c=input('请输入第三个整数：')
    a=int(a)
    b=int(b)
    c=int(c)
    is_triangle(a,b,c)

caution_input()

