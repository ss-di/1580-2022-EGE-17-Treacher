k = 12
d = list(map(int, open('1.txt').readlines()))

n = d[0]
del d[0]

m = [0] * k
m[0] = 0

cnt = 0
for x in d:
    r = x % k
    m2 = m.copy()
    m2[r] += 1
    for i in range(k):
        if m[i] > 0:
            m2[(i+r)%k] += m[i]
    m = m2
    cnt += m[(k-r)%12]
    print(x, m)

print(m[0])

'''
4
5 +
7 
12
23

0 2
1
2
3
4
5 1
6
7 1
8
9
10
11 1

+1 +2
'''