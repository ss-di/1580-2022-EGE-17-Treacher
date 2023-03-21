m = list(map(int, open('17-3.txt').readlines()))

cnt = 0
mn19 = min(filter(lambda x: x > 0 and x % 19 == 0, m))
mx = -10**100

for i in range(len(m)-1):
    x, y = m[i], m[i+1]
    if x + y < mn19:
        cnt += 1
        mx = max(mx, x + y)
print(cnt, mx)

