def gcd(a,b):
    if b==0:
        return a
    else :
        r=a%b
        a=b
        b=r
        return gcd(a,b)

print(gcd(2,8))