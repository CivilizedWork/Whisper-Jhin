def avoids(word1,word2):
    for line1 in word1:
        if line1 in word2:
            return False
    return True

#print(avoids('true','wozk'))
def print_avoids(word):
    fin = open('words.txt')
    a=0
    for letter in fin:
        if avoids(letter,word):
            a=a+1
    print(a)

print_avoids('uuuu')