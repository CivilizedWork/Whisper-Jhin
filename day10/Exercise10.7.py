def has_duplicates(t):
    a = 0
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] == t[j]:
                a = a+1
    if a>len(t):
        return True
    else:
        return False

t = ['a', 'c', 'd', 'e', 'f']
print(has_duplicates(t))