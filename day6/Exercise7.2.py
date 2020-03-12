import math
def eval_loop():
    t = input('请输入值（只有输入done时才会结束程序）')
    while t!='done':
        a=eval(t)
        print(a)
        t = input('请输入值（只有输入done时才会结束程序）')
    print(a)

eval_loop()