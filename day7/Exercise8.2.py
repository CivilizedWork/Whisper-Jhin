def count(word,a):
    index = 0
    for letter in word:
        if letter ==a:
            index = index +1
    return index

print(count('banana','a'))