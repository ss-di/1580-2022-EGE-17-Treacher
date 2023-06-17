fn = "27_0.txt"
fn = "27_A.txt"
fn = "27_B.txt"

with open(fn) as f:
    data = f.readlines()
print(data[:2], data[-2:])
data = list(map(int, data))
print(data[:2], data[-2:])
n = data[0]
del data[0]
print(n, len(data), data[:2], data[-2:])

#data = [1, 2, 3, 4, 5, 6, 7]

data = data + data

pdata = [0]
for i in range(n*2):
    pdata.append(pdata[-1] + data[i])

mx = -1
for i in range(n):
    if i % 10 == 0:
        print(i / n * 100, mx)
    for j in range(i+2, n-1+i):
        sf1 = pdata[j] - pdata[i]
        sf2 = pdata[j+n-(j-i)] - pdata[j]
        s1 = data[i] + data[j-1]
        s2 = data[j] + data[j+n-(j-i)-1]
        if sf1 % s1 == 0 and \
           sf2 % s2 == 0 and \
           s1 + s2 > mx:
            mx = s1 + s2
print(mx)
'''
1 2 3 4 5 6 7 1 2 3 4 5 6 7 
0 1 3 6 10
'''