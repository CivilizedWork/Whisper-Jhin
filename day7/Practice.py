fruit = 'banana'
letter = fruit[1]
print(letter)
letter = fruit[0]
print(letter)
i = 1
print(fruit[i])
print(fruit[i+1])
# letter = fruit[1.5]
# print(letter)
fruit = 'banana'
print(len(fruit))
length = len(fruit)
# last = fruit[length]
# print(last)
last = fruit[length-1]
print(last)
index = 0
while index < len(fruit):
    letter = fruit [index]
    print(letter)
    index = index +1
def reverse_out(a):
    i = -1
    while i >= -len(a):
        reverse = a[i]
        print(reverse)
        i = i - 1

reverse_out('string')
for letter in fruit:
    print(letter)

prefixes = 'JKMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter+suffix)

s = 'Monty Python'
print(s[0:5])
print(s[6:12])
fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print(fruit[:])
greeting = 'Hello,world!'
# greeting[0] = ']'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
def find (word, letter):
    index =0
    while index <len(word):
        if word[index] == letter:
            return index
        index = index +1
    return -1
print(find('kfc','c'))
def find_3(word,letter,a):
    index = 0
    print(word[a])
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

find_3('kadf','ad',3)
word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count +1
print(count)
def count(word,rt):
    a = 0
    for letter in word :
        if letter == rt:
            a = a+1
    print(a)

count ('redivider','e')
word = 'banaan'
new_word = word.upper()
print(new_word)
index = word.find('a')
print(index)
print(word.find('na'))
print(word.find('na',3))
name = 'bob'
print(name.find('b',1,2))
print('a' in 'banana')
print('seed' in 'banana')
def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('jacklove','montypython')
if word =='banana':
    print('All right ,banana.')
if word <'banana':
    print('Your word :'+word+',comes before banana.')
elif word >'banana':
    print('Your word:'+word+',comes after banana.')
else:
    print('All right,bananas.')

def is_reverse(word1,word2):
    if len(word1)!=len(word2):
        return False
    i=0
    j=len(word2)-1
    while j>0:
        print(i,j)
        if word1[i]!=word2[j]:
            return False
        i=i+1
        j=j-1

    return True

print(is_reverse('pots','stop'))