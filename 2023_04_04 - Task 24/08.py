s = open("z5.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

ss = 'XZZY'

#s = 'XZZYaaaaXZZY'

cur = mx = 0
i = 0
while (i < len(s)):
    if s[i: i+len(ss)] != ss:
        cur += 1
        mx  = max(mx, cur)
        i += 1
    else:
        mx  = max(mx, cur+3)
        cur = 0
        i += 1

print(mx)

m = s.split(ss)
lens = list(map(len, m))
print(max(lens)+6) # если максимум в середине строки