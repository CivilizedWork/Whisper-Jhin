def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
"""
检验字符串s中的每一个字母是否都是小写字母，如果是，返回True，否则返回False
"""
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
"""
检验字符串s中的每一个字母是否都是小写字母，如果是，返回True，否则返回False
"""
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
"""
检验字符串s中的每一个字母是否都是小写字母，如果是，返回True，否则返回False
"""
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
"""
检验字符串s中是否包含小写字母。
"""
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
"""
检验字符串s中的每一个字母是否都是小写字母，如果是，返回True，否则返回False
"""
print(any_lowercase5('TEFe'))