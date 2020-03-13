def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def rotate_word(word,a):
    if word.islower():
        for letter in word:
            b = ord(letter)
            b = b + a
            print(chr(b), end='')
    elif not word.islower():
        for letter in word:
            b = ord(letter)
            b = b - a
            print(chr(b), end='')
rotate_word('IBm',1)