s = open("z4.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

ss = 'XYZ'
frag = ''
for i in range(len(s)):
    if frag in s:
        print(i, frag)
        frag += ss[i % len(ss)]
    else:
        break

mx = 0
for st in range(len(ss)):
    cur = 0
    for i in range(st, len(s), len(ss)):
        if s[i : i+len(ss)] == ss:
            cur += 1
            mx = max(mx, cur * len(ss))
        else:
            if s[i: i+2] == 'XY':
                mx = max(mx, cur * len(ss) + 2)
            elif s[i] == 'X':
                mx = max(mx, cur * len(ss) + 1)
                
            cur = 0
            
print(mx)
