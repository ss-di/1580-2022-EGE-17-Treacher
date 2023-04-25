fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'
with open(fn) as f:
    data = f.readlines()

data = list(map(int, data))

n = data[0]
del data[0]

print(n, data[:5])

k = 43
psum = [0]
lmax = [-1] * k
lmin = [n+1] * k
lmin[0] = 0

for x in data:
    psum.append(psum[-1] + x)
    lmax[psum[-1] % k] = max(lmax[psum[-1] % k], len(psum)-1)
    lmin[psum[-1] % k] = min(lmin[psum[-1] % k], len(psum)-1)

print(lmin)
print(lmax)

mxsum = -1
mnlen = n+1
for i in range(k):
    if lmin[i] != n+1 and lmax[i] != -1:
        if psum[lmax[i]] - psum[lmin[i]] > mxsum or \
           psum[lmax[i]] - psum[lmin[i]] == mxsum and lmax[i] - lmin[i] < mnlen:
            mxsum = psum[lmax[i]] - psum[lmin[i]]
            mnlen = lmax[i] - lmin[i]
            
print(mnlen, mxsum)
