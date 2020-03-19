def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams():
    fin = open('words.txt')
    d = dict()
    for line in fin :
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def print_anagram_sets(d):
    for v in d.values():
        if len(v)>1:
            print(len(v),v)

def print_anagram_sets_in_order(d):
    t = []
    for v in d.values():
        if len(v)>1:
            t.append((len(v),v))
    t.sort()
    for x in t:
        print(x)

def filter_length(d,n):
    res = {}
    for word,anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res

print_anagram_sets(all_anagrams())
print_anagram_sets_in_order(all_anagrams())
print(filter_length(all_anagrams(),8))