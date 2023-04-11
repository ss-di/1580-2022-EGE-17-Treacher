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
    return dels

A = 77_777_777
B = 88_888_888
for x in range(A, B+1):
    if x % 10000 == 0:
        print((x-A)/(B-A)*100)
    while (x % 2 == 0):
        x //= 2
    dels = get_dels(x)
    cnt = 0
    for d in dels:
        if d % 2 != 0:
           cnt += 1
    if cnt == 5:
        print(x, dels[1])
