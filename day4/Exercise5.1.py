import time
t=time.time()
def print_s():
    print('纪元以来经过了', end=' ')
    print(t, end=' ')
    print('秒')

def print_m():
    print('纪元以来经过了', end=' ')
    print(t//60, end=' ')
    print('分钟')

def print_h():
    print('纪元以来经过了', end=' ')
    print(t // 60//60, end=' ')
    print('小时')

def print_d():
    print('纪元以来经过了', end=' ')
    print(t // 60//60//24, end=' ')
    print('天')

print_d()
print_h()
print_m()
print_s()