import math
x = 2
if x > 0:
    y = math.log(x)
else:
    y = float('nan')

y = math.log(x) if x > 0 else float('nan')
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
def __init__(self, name, contents=None):
    self.name = name
    if contents == None:
        contents = []
    self.pouch_contents = contents

def __init__(self, name, contents=None):
    self.name = name
    self.pouch_contents = [] if contents == None else contents


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_all(t):
    return [s.capitalize() for s in t]

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def only_upper(t):
    return [s for s in t if s.isupper()]

g = (x**2 for x in range(5))
for val in g:
    print(val)

print(sum(x**2 for x in range(5)))
print(any([False, False, True]))
print(any(letter == 't' for letter in 'monty'))
def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract(d1, d2):
    return set(d1) - set(d2)

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def has_duplicates(t):
    return len(set(t)) < len(t)

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_only(word, available):
    return set(word) <= set(available)

from collections import Counter
count = Counter('parrot')
print(count)

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

count = Counter('parrot')
for val, freq in count.most_common(3):
    print(val, freq)

from collections import defaultdict
d = defaultdict(list)
t = d['new key']
print(t)
t.append('new value')
print(t)
def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d.setdefault(t, []).append(word)
    return d


def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x, p.y)
class Pointier(Point):
    """

    """

def printall(*args):
    print(args)

printall(1, 2.0, '3')
#printall(1, 2.0, third='3')
def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, third='3')
