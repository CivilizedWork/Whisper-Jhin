def uses_only(word,available):
    for letter in word:
        if letter not in available:
            return False
    return True

fin = open('words.txt')
for letter in fin:
    word = letter.strip()
    if uses_only(word,'acefhlo'):
        print(word)