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
x = 3
while x**4 <= B:
    if is_prime(x):
        tmp = x ** 4
        while tmp <= B:
            if tmp >= A:
                print(tmp)
            tmp *= 2
    x += 2
