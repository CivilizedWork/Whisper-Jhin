fout = open('output.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)
#fout.close()
x = 52
fout.write(str(x))
camels = 42
print(type('%d' % camels))
print('I have spotted %d camels.' % camels)
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camles'))
#'%d %d %d' % (1, 2)
#'%d' % 'dollars'
import os
cwd = os.getcwd()
print(cwd)
print(os.path.abspath('words.txt'))
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.listdir(cwd))
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


import os


def walk(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the version in the book.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the exercise solution, which uses os.walk.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


if __name__ == '__main__':
    walk('.')
    walk2('.')
#fin = open('bad_file')
#fout = open('/etc/passwd','w')
try:
    fin = open('bad_file')
except:
    print('Something went wrong.')
import dbm
db = dbm.open('captions','c')
db['cleese.png'] = 'Photo of Jhon Cleese.'
print(db['cleese.png'])
db['cleese.png'] = 'Photo of Jhon Cleese doing a silly walk.'
print(db['cleese.png'])
for key in db:
    print(key,db[key])
db.close()
import pickle
t = [1,2,3]
print(pickle.dumps(t))
t1 = [1,2,3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)
print(t1 == t2 )
print(t1 is t2)
cmd = 'ls-1'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(stat)
filename = 'book.tex'
cmd = 'md5sum' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)
def linecount(filename):
    count = 0
    for line in open(filename):
        count +=1
    return count

print(linecount('Practice.py'))
if __name__ == '__main__':
    print(linecount('Practice.py'))
s = '1 2\t 3\n  4'
print(s)
print(repr(s))

