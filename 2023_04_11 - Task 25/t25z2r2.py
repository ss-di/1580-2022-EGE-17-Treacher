def get_dels(x):
    dels = []
    d = 1
    while d*d <=:
        if x % d == 0:
            dels.append(d)
    return dels

A = 77_777_777
B = 88_888_888
for x in range(A, B+1):
    dels = get_dels(x)
    cnt = 0
    for d in dels:
        if d % 2 != 0:
           cnt += 1
    if cnt == 5:
        print(x, dels[1])
