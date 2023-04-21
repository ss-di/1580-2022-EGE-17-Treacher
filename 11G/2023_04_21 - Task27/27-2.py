def getpow2(x):
    res = 0
    while x % 2 == 0:
        res += 1
        x = x // 2 
    return min(res, 10)

with open('27-B.txt') as f:
    data = f.readlines()
    
n = int(data[0])
del data[0]
data = list(map(int, data))

print(n, data)

p = [[0] * 11 for i in range(3)]

ans = 0
for x in data:
    ans += sum(p[(3 - x % 3) % 3][10-getpow2(x):])
    p[x % 3][getpow2(x)] += 1
    
print(ans)