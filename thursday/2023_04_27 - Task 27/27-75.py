fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'

with open(fn) as f:
    data = f.readlines()
    
data = list(map(int, data))

n = data[0]
del data[0]

print(n, data[:2], data[-2:])

mxsum = -1
mnlen = n+1
k = 43

for b in range(n):
    for e in range(b, n):
#        print(b, e)
        csum = sum(data[b:e+1])
        clen = e - b + 1 # len(data[b:e+1])
        if csum % k == 0 and (csum > mxsum or csum == mxsum and clen < mnlen):
            mxsum = csum
            mnlen = clen

print(mnlen, mxsum)
