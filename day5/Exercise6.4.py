def is_power(a,b):
    if a==b:
        return True
    elif a%b==0:
        a=a/b
        return is_power(a,b)
    else:
        return False

print(is_power(27,3))