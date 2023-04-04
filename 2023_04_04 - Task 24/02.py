s = open("24.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

cur = mx = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1
print(mx)