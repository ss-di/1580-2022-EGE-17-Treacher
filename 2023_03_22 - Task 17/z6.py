def count_del(x):
    cnt = 0
    d = 1
    while d*d <= x:
        if x % d == 0:
            cnt += 2
        if x * x == d:
            cnt -= 1
        d += 1
    return cnt

cnt = 0
mn = 100000

for i in range(10001, 50000+1):
    if i % 1000==0:
        print(i)
    if count_del(i) > 17:
        cnt += 1
        mn = min(mn, i)

print(cnt, mn)
