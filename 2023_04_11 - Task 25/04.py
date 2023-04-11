def get_dels(x):
    ans = []
    d = 1
    while d*d < x:
        if x % d == 0:
            ans.append(d)
            ans.append(x // d)
        d += 1
    if d * d == x:
        ans.append(d)
    ans.sort()
    return ans

A = 77_777_777
B = 88_888_888

for x in range(A, B+1):
    if x % 10000 == 0:
        print((x-A)/(B-A)*100)
    while x % 2 == 0:
        x //= 2
    dels = get_dels(x)
    cnt = 0
    for d in dels:
        if d % 2 != 0:
            cnt += 1
    if cnt == 5:
        print(x, dels[1])