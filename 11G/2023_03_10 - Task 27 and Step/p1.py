f = open('27-75b.txt')
n = int(f.readline())

d = 43
p = []
ps = [0]


for i in range(n):
    x = int(f.readline())
    p.append(x)
    ps.append(ps[-1] + x)

ms = -1
for i in range(n):
    for j in range(i + 1, n + 1):
        s = ps[j] - ps[i]
        if s % 43 == 0:
            if s > ms:
                ms = s
                ln = j - i
            elif s == ms and j - i < ln:
                ln = j - i

print(ms, ln)
    
'''
7
21
13
9
19
17
26
95
'''