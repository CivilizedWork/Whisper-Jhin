def make_dict():
    fin = open('words.txt')
    s = dict()
    for letter in fin:
        word = letter.strip()
        s[word] = None
    return s

from pronounce import read_dictionary
fin = open('words.txt')
for line in fin:
    word = line.strip()
    f = word
    if len(word) == 5:
        m = word[1:]
        n = word[0]+word[2:]
        if read_dictionary(f)==read_dictionary(m) and read_dictionary(f)==read_dictionary(t):
            print(f)



