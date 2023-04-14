def avt(n):
    n2 = bin(n)[2:]
    s = n2.count('1')
    if s % 2 == 0:
        return '1' + n2[2:] + '0'
    else:
        return '11' + n2[2:] + '1'

ans = []
for n in range(1000):
    res = int(avt(n), 2)
    if res > 49:
        ans.append((res, n))
        print(res, n)
        
print(min(ans))
