fin = open('words.txt')
def method1():
    t = []
    for letter in fin:
        word = letter.strip()
        t.append(word)

    return t

def method2():
    t = []
    for letter in fin:
        word = letter.strip()
        t = t+[word]
    return t

print(method1())
print(method2())
"""
第二种慢得多，因为需要创建新的列表
"""