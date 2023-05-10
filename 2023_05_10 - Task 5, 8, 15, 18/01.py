def prime(x):
    if x == 1: return False
    for d in range(2, x//2 + 1):
        if x % d == 0:
            return False
    return True
    

def avt(x):
    s = str(x)
    v = []
    v.append(int(s[0]+s[1]))
    v.append(int(s[0]+s[2]))
    v.append(int(s[1]+s[0]))
    v.append(int(s[1]+s[2]))
    v.append(int(s[2]+s[0]))
    v.append(int(s[2]+s[1]))
    cnt = 0
    for i in v:
        if i >= 10 and prime(i):
            cnt += 1
    return cnt

mx = -1
for i in range(100, 1000):
    cur = avt(i)
    if cur >= mx:
        mx = cur
        mxi = i
print(mxi)
