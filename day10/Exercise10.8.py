import random
def has_duplicates(t):
    a = 0
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i] == t[j]:
                a = a+1
    if a>len(t):
        return True
    else:
        return False

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1,365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count

def main():
   num_students = 23
   num_simulations = 1000
   count = count_matches(num_students, num_simulations)
   print('After %d simulations' % num_simulations)
   print('with %d students' % num_students)
   print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()
