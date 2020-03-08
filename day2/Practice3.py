print(type(42))
#python提供了内建函数。
#函数int接受任何值，并在其能做到的情况下，将该值转换成一个整型数，否则会报错。
print(int('32'))
#print(int('Hello'))
#int能将浮点数转换为整型数，但是他并不进行舍入；这是截掉了小数点部分。
print(int(3.99999))
print(int(-2.3))
#float可以将整型数和字符串转换为浮点数。
print(float(32))
print(float('3.14159'))
#string可以将实参转换成字符串。
print(str(32))
print(str(3.14159))
import math
print(math)
#点标记法
#ratio=signal_power/noise_power
#decibels=10*math.log10(ratio)
radians=0.7;
height=math.sin(radians)
degrees=45
radians=degrees/180.0*math.pi
print(math.sin(radians))
x=math.sin(degrees/360.0*2*math.pi)
x=math.exp(math.log(x+1))
#minutes=hours*60
#hours*60=minutes
#函数定义的第一行被称作函数头（header）； 其余部分被称作函数体（body）。 函数头必须以冒号结尾，而函数体必须缩进。 按照惯例，缩进总是4个空格。 函数体能包含任意条语句。
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack,and I'm okay.")
    print("I sleep all night and I work all day")

#print(print_lyrics())
#print(type(print_lyrics()))
repeat_lyrics()
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')
print_twice(42)
print_twice(math.pi)
print_twice('Sapm'*4)
print_twice(math.cos(math.pi))
michael='Eric,the half a bee.'
print_twice(michael)
def cat_twice(part1,part2):
    cat=part1+part2
    print_twice(cat)

line1='Bing tiddle'
line2='tiddle bang.'
cat_twice(line1,line2)
#print(cat)
x=math.cos(radians)
golden=(math.sqrt(5)+1)/2
print(math.sqrt(5))
math.sqrt(5)
result=print_twice('Bing')
print(result)
print(type(None))


