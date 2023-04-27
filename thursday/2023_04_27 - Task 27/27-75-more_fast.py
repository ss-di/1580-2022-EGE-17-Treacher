fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'

with open(fn) as f:
    data = f.readlines()
    
data = list(map(int, data))

n = data[0]
del data[0]

print(n, data[:2], data[-2:])

pr = [0]
for x in data:
    pr.append(pr[-1] + x)

#print(data)
#print(pr)

mxsum = -1
mnlen = n+1
k = 43

for b in range(n):
    for e in range(b, n):
#        print(b, e)
        csum = pr[e+1] - pr[b]
        clen = e - b + 1 # len(data[b:e+1])
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