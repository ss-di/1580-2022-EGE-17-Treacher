def count_del(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
        if cnt > 17:
            return cnt
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
#6585 10008
#6585 10008