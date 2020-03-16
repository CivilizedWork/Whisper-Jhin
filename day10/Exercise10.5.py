def is_sorted(t):
    for i in range(len(t)):
        if t[i]<=t[i+1]:
            return True
        else:
            return False

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))