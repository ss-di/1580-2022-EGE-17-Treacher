fn = '27-75.txt'
fn = '27-75a.txt'
#fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

data = list(map(int, data))

n = data[0]
del data[0]
print(n, data[:3], data[-3:])

k = 43
maxs = -1
minl = n+1
for i in range(n):
    for j in range(i+1, n):
        s = sum(data[i:j+1])
        if s % k == 0 and (s > maxs or s == maxs and j - i + 1 < minl):
            maxs = s
            minl = j - i + 1
            
print(minl, maxs)