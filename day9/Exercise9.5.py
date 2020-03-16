def use_all(word,required):
    for letter in required:
        if letter not in word:
            return False
    return True

print(use_all('aeiou','aeio'))
def uses_only(word,available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word,required):
    return uses_only(required,word)