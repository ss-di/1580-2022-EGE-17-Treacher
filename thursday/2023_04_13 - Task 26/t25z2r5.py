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
    
    
A = 35_000_000
B = 40_000_000
for x in range(A, B+1):
    tmp = x
    while (x % 2 == 0):
        x //= 2
    x4 = round(math.sqrt(math.sqrt(x)))
    if  x4 ** 4 == x and is_prime(x4):
        print(tmp)
