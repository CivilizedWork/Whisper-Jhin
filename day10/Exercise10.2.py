def cumsum(t):
    s = []
    for i in range(len(t)):
        s.append(sum(t[:i+1]))
    return s

t = [1, 2, 4,5]
print(cumsum(t))
