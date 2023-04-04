s = open("24-5.txt").readline()

print(s[:5])
print(s[-3:])
s = s[:-1]
print(s[:5])
print(s[-3:])

for i in range(1, len(s)):
    if '('*i in s:
        print(i)
    else:
        break
    
cur = 0
mx = 0
for c in s:
    if c == '(':
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0

print(mx)