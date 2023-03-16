def osn(x):
    digs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(digs)-1, 0, -1):
        if digs[i] in x:
            return i+1
    return 0

d = open('17-362.txt').readlines()

cnt = 0
mn = mx = None
#mn = +10**10000
#mx = -10**10000
for i in range(len(d)-1):
    o1 = osn(d[i])
    o2 = osn(d[i+1])
    if abs(o1 - o2) <= 2:
        cnt += 1
        s = int(d[i], o1) + int(d[i+1], o2)
        if mn == None or s < mn: mn = s
        if mx == None or s > mx: mx = s
        
print(cnt, mn, mx)