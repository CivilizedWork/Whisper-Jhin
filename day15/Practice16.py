class Time :
    """Represents the time of day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30
def print_time(time):
    print('%.2d' % time.hour,end=':')
    print('%.2d' % time.minute,end=':')
    print('%.2d' % time.second)

def is_after(t1, t2):
    if t1.hour>t2.hour:
        return True
    elif t1.hour == t2.hour and t1.minute >t2.minute:
        return True
    elif t1.hour == t2.hour and t1.minute == t2.minute and t1.second>t2.second:
        return True
    else:
        return False
print_time(time)
def add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def increment(time, seconds):
    time.second += seconds
    if seconds<60:
        if time.second >= 60:
            time.second -= 60
            time.minute += 1

        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1
    else:
        time.minute += 1
        seconds -=60
        increment(time,seconds)


import copy
def increment(time1, seconds):
    time2 = copy.copy(time1)
    time2.second += seconds
    if seconds < 60:
        if time2.second >= 60:
            time2.second -= 60
            time2.minute += 1

        if time2.minute >= 60:
            time2.minute -= 60
            time2.hour += 1
    else:
        time2.minute += 1
        seconds -= 60
        increment(time2, seconds)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(t1,seconds):
    seconds1 = time_to_int(t1) + seconds
    return int_to_time(seconds1)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)