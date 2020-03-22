class Time:
    """Represents the time of day."""

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

class Time:
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

start = Time()
start.hour = 9
start.minute = 45
start.second = 00
print_time(start)
Time.print_time(start)
start.print_time()
start.print_time()
end = start.increment(1337)
end.print_time()
print(end.is_after(start))
time = Time()
time.print_time()
time = Time (9)
time.print_time()
time = Time(9, 45)
time.print_time()
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '%.2d,%.2d' % (self.x, self.y )

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return

    def __add__(self, other):
        if isinstance(other, Point):
            self.x = self.x + other.x
            self.y = self.y + other.y
            return
        else:
            new = Point()
            new.x = self.x + other[0]
            new.y = self.y + other[1]
            return new

    def __radd__(self, other):
        return self.__add__(other)

time = Time(9, 45)
print(time)
start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)
t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)
p = Point(3,4)
print(vars(p))
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))