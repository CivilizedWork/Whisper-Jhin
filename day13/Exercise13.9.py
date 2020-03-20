def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def cumsum(t):
    s = []
    for i in range(len(t)):
        s.append(sum(t[:i+1]))
    return s

fin = open('emma.txt')
import math
def tye(h):
    t = []
    b = []
    for key in h:
        t.append(key)
        b.append(h[key])
    s = cumsum(b)
    n = b[len(b)-1]
    for r in  range(len(s)):
        m = s[r+1]/n
        t.reverse()
        print(t)
        print(math.log(m),math.log(r))

tye(histogram(fin))