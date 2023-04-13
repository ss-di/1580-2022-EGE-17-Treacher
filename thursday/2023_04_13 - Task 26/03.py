with open('26-106.txt') as f:
    data = f.readlines()

n, m, k = list(map(int, data[0].split()))
print(n, m, k)
del data[0]

data2 = []
for d in data:
    data2.append(list(map(int, d.split())))

data2.sort()
print(data2[:10])

#zal = [[0]*10000 for i in range(10000)]
zal = [[0]*m for i in range(n)]
print('done')

for d in data:
    a, b = list(map(int, d.split()))
    zal[a-1][b-1] = 1

ans = 0
maxr = -1
maxm = 0
for i in range(n):
    if zal[i][0] == 1 and zal[i][1] == 0:
        zal[i][1] = 2
    for j in range(1, m-1):
        if zal[i][j] == 1:
            if zal[i][j-1] == 0:
                zal[i][j-1] = 2
            if zal[i][j+1] == 0:
                zal[i][j+1] = 2
    if zal[i][m-1] == 1 and zal[i][m-2] == 0:
        zal[i][m-2] = 2
    cur = zal[i].count(0)
    ans += cur
    if cur > maxm:
        maxm = cur
        maxr = i+1

print(ans, maxr)