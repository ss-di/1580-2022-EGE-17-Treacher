f = open('17-1.txt')
m = f.readlines()
f.close()
m = list(map(int, m))
print(m)

cnt = 0
mn = 10**1000

for i in range(len(m)-1):
    a, b = m[i], m[i+1]
    if a % 7 == 0 and b % 17 != 0 or \
       b % 7 == 0 and a % 17 != 0:
        cnt += 1
        mn = min(mn, a + b)
print(cnt, mn)