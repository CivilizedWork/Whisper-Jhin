def make_dict():
    fin = open('words.txt')
    s = dict()
    for letter in fin:
        word = letter.strip()
        s[word] = None
    return s

print(make_dict())
print('aahe' in make_dict())