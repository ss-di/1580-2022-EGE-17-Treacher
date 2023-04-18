with open('26-97.txt') as f:
    data = f.readlines()
print(data)

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))
    data[i] = [data[i][0]-2*data[i][1]] + data[i]
    
print(n, data)

data.sort(reverse=True)

print(n, data)

cnt = 1
last = data[0]
pack = [last]
for x in data:
    if x[1] <= last[0]-3:
        cnt += 1
        last = x
        pack.append(x)
mx = 0
for x in data:
    if x[1] <= pack[-2][0]-3:
        mx = max(mx, x[1])
print(cnt, last, mx)