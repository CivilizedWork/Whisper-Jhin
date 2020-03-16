fin = open('words.txt')
def method1():
    t = []
    for letter in fin:
        word = letter.strip()
        t.append(word)

    return t

def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True

def search():
    for letter in method1():
        if is_palindrome(letter):
            print(letter)

search()