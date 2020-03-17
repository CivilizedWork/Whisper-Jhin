def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

print(ack(3,4))
def ack_new(m,n):
    known_1 = {0: n+1}
    known_2 = {0: 1}
    if m in known_1:
        return known_1[m]
    elif n in known_2:
        return ack_new(m-1, known_2[n])
    else:
        return ack_new(m-1, ack_new(m, n-1))

print(ack_new(3, 6))