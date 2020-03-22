def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
class Time :
    """Represents the time of day.

    attributes: hour, minute, second
    """
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(t1, n):
    assert valid_time(t1)
    seconds = time_to_int(t1)*n
    return int_to_time(seconds)

def v(t1, d):
    return mul_time(t1, 1/d)
