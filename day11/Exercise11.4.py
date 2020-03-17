def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def has_duplicates_new(t):
    delimiter = ''
    s = delimiter.join(t)
    d = histogram(s)
    for key in d :
        if d[key]>=2:
            return True
        else:
            return False

t = ['a', 'c', 'd', 'e', 'f']
print(has_duplicates_new(t))