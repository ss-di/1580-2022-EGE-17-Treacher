s = open('24-153.txt').readline()

print(1, s[:3])
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])
#s = 'EFEEEEEEEEEttttt'
s2 = 'EEEE'
s3 = s.split(s2)
mx = 0
for i in range(len(s3)):
    mx = max(mx, len(s3[i]))
    mxi = i
print(mx+3, i, len(s3))
print(s3[mxi][:4])


mx = cur = 0
for i in range(len(s)):
    if s[i : i+len(s2)] != s2:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0
print(mx)
