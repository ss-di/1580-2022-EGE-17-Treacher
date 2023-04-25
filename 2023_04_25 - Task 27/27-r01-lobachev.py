fn = '27-r01.txt'
#fn = '27-75a.txt'
#fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

n = int(data[0])
del data[0]

for i in range(n):
    data[i] = list(map(int, data[i].split()))

print(n, data[:5])
print(n, data[n-2:])
del data[-1]
print(n, data[n-2:])

k = 6
mxsum = 0
diff = []
for a, b in data:
    mxsum += max(a, b)
    if abs(a-b) % k != 0:
        diff.append(abs(a-b))
        
print(mxsum, mxsum % k)

diff.sort()

INF = mxsum + 1
bestdiff = [INF] * k
bestdiff[0] = 0

for d in diff:
    bestdiff2 = bestdiff.copy()
    for i in range(k):
        if bestdiff[i] != INF:
            bestdiff2[(i + d) % k] = min(bestdiff2[(i + d) % k], bestdiff[i] + d)
    bestdiff = bestdiff2
print(bestdiff)
if bestdiff[mxsum % k] != INF:
    mxsum -= bestdiff[mxsum % k]
    print(mxsum, mxsum % k)
else:
    print('-1')