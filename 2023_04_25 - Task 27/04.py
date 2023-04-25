fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

data = list(map(int, data))

n = data[0]
del data[0]
print(n, data[:3], data[-3:])

ps = [0]
for x in data:
    ps.append(ps[-1] + x)

#print(data)
#print(ps)

k = 43

maxs = -1
minl = n+1
for i in range(n):
    for j in range(i+1, n):
        s = ps[j+1] - ps[i]
        if s % k == 0 and (s > maxs or s == maxs and j - i + 1 < minl):
            maxs = s
            minl = j - i + 1
            
print(minl, maxs)

'''
0 1 2 3 4 5
1 2 3 4 5 6

0 1 2 3 4  5  6
0 1 3 6 10 15 21

'''