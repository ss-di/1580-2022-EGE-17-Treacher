def to9(x):
    ans = ''
    while x:
        ans = str(x % 9) + ans
        x = x // 9
    return ans

cnt = 0
for x in range(10**90):
    x9 = to9(x)
    if len(x9) > 7:
        break
    if len(x9) == 7:
        if x9.count('8') == 1 and \
           int(x9[0]) % 2 == 0 and \
           int(x9[-1]) % 2 != 0:
            cnt += 1
            print(x9)
        
print(cnt)
