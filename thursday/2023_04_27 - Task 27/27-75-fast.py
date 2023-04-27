fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'

with open(fn) as f:
    data = f.readlines()
    
data = list(map(int, data))

n = data[0]
del data[0]

print(n, data[:2], data[-2:])

k = 43

pr = [0]
minl = [n+1] * k
minl[0] = 0

for x in data:
    pr.append(pr[-1] + x)
    minl[pr[-1] % k] = min(minl[pr[-1] % k], len(pr)-1)

#print(data)
#print(pr)
#for i in range(k):
#    if minl[i] != n+1:
#        print(i, minl[i])

mxsum = -1
mnlen = n+1

for e in range(n):
    csum = pr[e+1]
    clen = e + 1
    ost = csum % k
    if minl[ost] != n+1:
        csum -= pr[minl[ost]]
        clen -= minl[ost]
        if csum % k == 0 and (csum > mxsum or csum == mxsum and clen < mnlen):
            mxsum = csum
            mnlen = clen

print(mnlen, mxsum)

'''
0  1  2  3  4  5
3  6  8  3  1  10

0  1  2  3  4  5  6
0  3  9  17 20 21 31

sum 2-4 = pr[4+1] - pr[2]



'''