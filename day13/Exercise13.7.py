import random
fin = open('emma.txt')
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def cumsum(t):
    s = []
    for i in range(len(t)):
        s.append(sum(t[:i+1]))
    return s

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word]*freq)

    return random.choice(t)

import bisect
def make_word_list():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    word_list = make_word_list()
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def random_word_new(h):
    t = []
    b = []
    for key in h:
        t.append(key)
        b.append(h[key])
    s = cumsum(b)
    n = b[len(b)-1]
    i = random.randint(1,n)
    c = in_bisect(s,i)
    d = t[c]
    print(d)

random_word_new(histogram(fin))