with open('26_7096.txt') as f:
    data = f.readlines()

n = int(data[0])
del data[0]
print(n, len(data))

data = list(map(int, data))

data.sort()

cnt = 1
last = data[0]
for i in range(1, n):
    if data[i] - last >= 11:
        cnt += 1
        last = data[i]
        
print(cnt)

x = 0
last = data[0]
cnt2 = cnt
while cnt2 == cnt:
    print(data[x])
    x += 1
    cnt2 = 1
    last = data[x]
    for i in range(x+1, n):
        if data[i] - last >= 11:
            cnt2 += 1
            last = data[i]
