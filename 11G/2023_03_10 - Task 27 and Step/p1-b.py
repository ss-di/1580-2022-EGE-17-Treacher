f = open('27-75b.txt')
n = int(f.readline())

d = 43
p = []
ps = [0]
mn_i = [-1] * d
mx_i = [-1] * d

for i in range(n):
    x = int(f.readline())
    p.append(x)
    ps.append(ps[-1] + x)

for i in range(n + 1):
    mx_i[ps[i] % d] = i
    if mn_i[ps[i] % d] == -1:
        mn_i[ps[i] % d] = i

ms = -1
for r in range(d):
    if mx_i[r] != -1:
        s = ps[mx_i[r]] - ps[mn_i[r]]
        if s > ms:
            ms = s
            ln = mx_i[r] - mn_i[r]
        elif s == ms and mx_i[r] - mn_i[r] < ln:
            ln = mx_i[r] - mn_i[r]
      
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