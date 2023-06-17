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

mx = -1
for i in range(n):
    if i % 1 == 0:
        print(i / n * 100)
    for j in range(i+2, n-1+i):
        p1 = data[i:j]
        p2 = data[j:j+n-len(p1)]
        s1 = p1[0] + p1[-1]
        s2 = p2[0] + p2[-1]
#        print(p1, p2)
        if sum(p1) % s1 == 0 and \
           sum(p2) % s2 == 0 and \
           s1 + s2 > mx:
            mx = s1 + s2
print(mx)
'''
1 2 3 4 5 6 7 1 2 3 4 5 6 7 
'''