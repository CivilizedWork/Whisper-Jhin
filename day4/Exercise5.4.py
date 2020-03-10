def recurse(n,s):
    """"调用该函数时，实参n必须大于0（不然就会发生无限递归），s要等于0 """
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3,0)
#1.
# 如果这样运行的话：recurse(-1,0),就会发生无限递归，报错。