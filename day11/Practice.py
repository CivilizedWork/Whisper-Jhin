eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
#print(eng2sp['four'])
print(len(eng2sp))
print('one' in eng2sp)
print('uno' in eng2sp)
vals = eng2sp.values()
print('uno' in vals)
def histogram(s):
    d = dict()
    for c in s:
        if c not in d :
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('brontosaurus')
print(h)
h = histogram('a')
print(h)
print(h.get('a',0))
print(h.get('b',0))
"""
def histogram(s):

h = histogram('brontosaurus')
print(h)
"""
def print_hist(h):
    for c in h:
        print(c,h[c])

h = histogram('parrot')
print_hist(h)
for key in sorted(h):
    print(key,h[key])
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')

h = histogram('parrot')
key = reverse_lookup(h,2)
print(key)
#key = reverse_lookup(h,3)
#print(key)
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)
t = [1,2,3]
d = dict()
#d[t] = 'oops'
known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1)+fibonacci(n-2)
    known[n] = res
    return res

verbos = True
def example1():
    if verbos:
        print('Running example1')

been_called = False
def example2():
    global been_called
    been_called = True

count = 0
def example3():
    global count
    count += 1

known = {0:0,1:1}
def example4():
    known[2] = 1

def example5():
    global known
    known = dict()
    