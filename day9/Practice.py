fin = open('words.txt')
print(fin.readline())
line = fin.readline()
word = line.strip()
print(word)
for line in fin:
    word = line.strip()
    print(word)

def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True

def is_palindrome(word):
    return is_reverse(word, word)