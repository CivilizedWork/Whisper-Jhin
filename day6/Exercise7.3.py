import math
def estimate_pi():
    k=0
    sum=0
    t = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))
    while t>=1e-15:
        t = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))
        sum=sum+t
        k=k+1

    pi=9801/(2*math.sqrt(2)*sum)
    return pi

print(estimate_pi())