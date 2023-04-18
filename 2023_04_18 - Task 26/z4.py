with open('26-97.txt') as f:
    data = f.readlines()
print(data)

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))
    
print(n, data)

for i in range(n):
    data[i][1] *= -1

data.sort(reverse=True)

for i in range(n):
    data[i][1] *= -1

print(n, data)

cnt = 1
last = data[0]
for x in data:
    if x[0] <= last[0] - last[1]*2 - 3:
        cnt += 1
        last = x

print(cnt, last)