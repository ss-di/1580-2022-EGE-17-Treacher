def osn(x):
#    digs = '0123456789'
#    for i in range(26):
#        digs += chr(ord('A') + i)

    digs = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    digs = sorted(digs)
    digs = ''.join(digs)
#    print(len(digs), digs)

#    for i in range(len(digs)-1, -1, -1):
#        if digs[i] in x:
#            return i+1
#    return 0

    return digs.index(max(x))+1
    
    
d = open('17-362.txt').readlines()

mx = -1
cnt = 0
for i in range(len(d)-1):
    a, b = d[i:i+2]
    oa = osn(a)
    ob = osn(b)
    if abs(oa - ob) <= 2:
        cnt += 1
        mx = max(mx, int(a, oa) + int(b, ob))
        
print(cnt, mx)