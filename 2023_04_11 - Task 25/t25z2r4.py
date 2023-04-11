import math

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
    if round(math.sqrt(math.sqrt(x))) ** 4 != x:
        continue
    dels = get_dels(x)
    cnt = 0
    for d in dels:
        if d % 2 != 0:
           cnt += 1
    if cnt == 5:
        print(tmp, dels[1])
