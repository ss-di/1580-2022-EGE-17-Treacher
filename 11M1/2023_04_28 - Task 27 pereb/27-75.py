fn = '27-75.txt'
fn = '27-75a.txt'
#fn = '27-75b.txt'
with open(fn) as f:
	data = f.readlines()
	
print(data[:2], data[-2:])

data = list(map(int, data))
print(data[:2], data[-2:])

n = data[0]
del data[0]
print(n, data[:2], data[-2:])

mxsum = -1
mnlen = n+1
for s in range(n):
	for e in range(s, n):
		su = sum(data[s:e+1])
		ln = e - s + 1
		if su % 43 == 0 and (su > mxsum or su == mxsum and ln < mnlen):
			mxsum = su
			mnlen = ln
print(mnlen, mxsum)
