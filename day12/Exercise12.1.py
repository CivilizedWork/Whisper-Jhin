def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def most_frequent(string):
    t = list(string)
    d = histogram(t)
    max = 1
    for key in d :
        if d[key]>max:
            max = d[key]
    i = max
    while i >=1:
        for key in d:
            if d[key] == i:
                print(key)
        i = i-1

most_frequent('risist')

