s = open("24-j1.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

p = '*'
cur = mx = 0
for i in range(len(s)):
    if (cur == 0 or p == 'Т') and s[i] == 'К' or \
       p == 'К' and s[i] == 'О' or \
       p == 'О' and s[i] == 'Т':
        cur += 1
        mx = max(mx, cur)
    else:
        if s[i] == 'К':
            cur = 1
        else:
            cur = 0
    p = s[i]
    
print(1, mx)

frag = 'К'
for i in range(1, len(s)+2):
    if frag in s:
        print(i, frag)
        frag = frag + 'КОТ'[i%3]
    else:
        break
    
print(225/3)