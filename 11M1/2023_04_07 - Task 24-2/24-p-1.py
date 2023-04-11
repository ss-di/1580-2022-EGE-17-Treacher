s = open('24.txt').readline()

print(s[:3])
print(s[-3:])
# s = s[:-1]
# print(s[-3:])

#s = 'ААAАВВВВ'

mx = 0
for st in range(3):
    cnt = 0
    for i in range(st, len(s), 3):
        s3 = s[i:i+3]
        if s3.count(s3[0]) == 3:
            cnt += 1
            mx = max(mx, cnt)
        else:
            cnt = 0
print(mx)