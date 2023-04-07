s = open('24.txt').readline()

print(1, s[:3])
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

s2 = 'ZZZZZZZ'
print(s2 in s)

s2 = ''
while s2 in s:
    print(len(s2), s2)
    s2 += 'Z'

cur = mx = 0
for i in range(len(s)):
    if s[i] == 'Z':
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0
print(mx)

