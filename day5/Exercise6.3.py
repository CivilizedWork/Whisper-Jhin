def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

#print(middle('nov'))
"""
当用一个两个字母的字符串和一个字母，空字符串调用 middle 时会返回一个None值
"""

def is_palindrome(word):
    if len(word)<=1:
        return True
    if first(word)!=last(word):
        return False
    word=middle(word)
    return is_palindrome(word)

print(is_palindrome('redivider'))