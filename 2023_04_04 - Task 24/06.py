s = open("24-153.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

#s = 'AEABEABEABEAB'

mx = 0
for st in range(len('EAB')):
    cur = 0
    for i in range(st, len(s), 3):
        if s[i:i+3] == 'EAB':
            cur += 1
            mx = max(mx, cur*3)
        else:
            if s[i:i+2] == 'EA':
                mx = max(mx, cur*3+2)
            elif s[i] == 'E':
                mx = max(mx, cur*3+1)
            cur = 0

print(mx)