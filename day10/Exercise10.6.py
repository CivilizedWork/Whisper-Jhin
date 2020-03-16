def is_anagram(word1,word2):
    t1 =list(word1)
    t2 =list(word2)
    t1.sort()
    t2.sort()
    if t1 == t2:
        return True
    else:
        return False

print(is_anagram('wired','riwea'))
