# 1
with open('17-2.txt') as f:
    m = f.readlines()
m = list(map(int, m))

m = list(map(int, open('17-2.txt').readlines()))

cnt = 0
mn = 10**10

for i in range(len(m)-1):
    x, y = m[i], m[i+1]
    if x % 7 == 0 and y % 17 != 0 or y % 7 == 0 and x % 17 != 0:
        cnt += 1
        mn = min(mn, x + y)
print(cnt, mn)

