fn = '27-r02.txt'
#fn = '27-75a.txt'
#fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

data = list(map(int, data))
n = data[0]
del data[0]

print(n, data[:5])
print(n, data[n-2:])

k = 12

ans = 0
cnt = [0] * k
for x in data:
    ans += cnt[(k - x % k) % k]
    cnt2 = cnt.copy()
    for i in range(k):
        cnt2[(i + x % k) % k] += cnt[i]
    cnt2[x % k] += 1
    cnt = cnt2
print(cnt)
print(cnt[0])

'''
i = 5
cnt[i] = 50
x = 10
(i + x) % k
'''