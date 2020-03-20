import random
for x in range(10):
    x = random.random()
    print(x)

print(random.randint(5,10))
print(random.randint(5,10))
t = [1,2,3]
print(random.choice(t))
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

t = ['a', 'b', 'a']
d = histogram(t)
def choose_from_hist(d):
    t1 = []
    for key in d:
        t1.append(key*d[key])
    return random.choice(t)

print(choose_from_hist(d))