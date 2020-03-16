fin = open('words.txt')
def has_no_e1(word):
    for letter in word:
        if letter == 'e':
            return False

    return True

print(has_no_e1('wired'))
def has_no_e2():
    a = 0
    b = 0
    for line in fin:
       a = a+1
       if has_no_e1(line):
            print(line)
            b = b+1

    print(b/a)

has_no_e2()