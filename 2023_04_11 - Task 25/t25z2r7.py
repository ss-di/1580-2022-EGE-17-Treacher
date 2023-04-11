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
    

A = 77_777_777
B = 88_888_888
ans = []
x = 3
while x**4 <= B:
    if  is_prime(x):
        tmp = x ** 4
        while tmp <= B:
            if tmp >= A:
                ans.append((tmp, x))
            tmp *= 2
    x += 2
ans.sort()
print(*ans, sep="\n")
