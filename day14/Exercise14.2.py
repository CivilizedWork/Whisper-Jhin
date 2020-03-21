import shelve
import sys
def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    fin = open(filename)
    d = dict()
    for line in fin :
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d



def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.

    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.

    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)
