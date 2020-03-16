def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

t = [1, 2, 3, 4,2,3]
chop(t)
print(t)