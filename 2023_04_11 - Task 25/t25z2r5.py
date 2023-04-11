import math


def is_prime(x):
    if x == 1:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True
    
    
def get_dels(x):
    dels = []
    d = 1
    while d*d < x:
        if x % d == 0:
            dels.append(d)
            dels.append(x // d)
        d += 1
    if x % d == 0:
        dels.append(d)
    dels.sort()
    return dels


A = 77_777_777
B = 88_888_888
for x in range(A, B+1):
    tmp = x
    while (x % 2 == 0):
        x //= 2
    x4 = round(math.sqrt(math.sqrt(x)))
    if  x4 ** 4 == x and is_prime(x4):
        dels = get_dels(x)
        print(tmp, dels[1])
