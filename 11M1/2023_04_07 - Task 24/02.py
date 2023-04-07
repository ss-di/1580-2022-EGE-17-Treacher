s = open('24-153.txt').readline()

print(1, s[:3])
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

s2 = 'EABEABE'
print(s2 in s)

s2 = 'EAB'*1000
s3 = ''
i = 0
while s3 in s:
    print(len(s3), s3)
    s3 += s2[i]
    i += 1