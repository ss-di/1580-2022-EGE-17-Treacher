fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

data = list(map(int, data))

n = data[0]
del data[0]
print(n, data[:3], data[-3:])

k = 43

minl = [n+1] * k
maxl = [-1] * k
minl[0] = 0
ps = [0]
for x in data:
    ps.append(ps[-1] + x)
    minl[ps[-1] % k] = min(minl[ps[-1] % k], len(ps)-1)
    maxl[ps[-1] % k] = max(maxl[ps[-1] % k], len(ps)-1)

#print(data)
#print(ps)

maxs = -1
mnl = n+1

for i in range(k):
    if maxl[i] != -1 and minl[i] != n+1:
        s = ps[maxl[i]] - ps[minl[i]]
        if s % k == 0 and (s > maxs or s == maxs and maxl[i] - minl[i] < mnl):
            maxs = s
            mnl = maxl[i] - minl[i]
            
print(mnl, maxs)

'''
0 1 2 3 4 5
1 2 3 4 5 6

0 1 2 3 4  5  6
0 1 3 6 10 15 21

'''