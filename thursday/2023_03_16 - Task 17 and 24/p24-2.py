s = open('24-157s.txt').readline()

print(len(s))

mx = 0
cur = 0

#0123456789

for i in range(0, len(s)-1, 3):
    if s[i:i+3] == 'EBA':
        cur += 3
        mx = max(mx, cur)
    else:
        if s[i:i+2] == 'EB':
            mx = max(mx, cur + 2)
        elif s[i+1] == 'E':
            mx = max(mx, cur + 1)
        cur = 0

cur = 0
for i in range(1, len(s)-1, 3):
    if s[i:i+3] == 'EBA':
        cur += 3
        mx = max(mx, cur)
    else:
        if s[i:i+2] == 'EB':
            mx = max(mx, cur + 2)
        elif s[i+1] == 'E':
            mx = max(mx, cur + 1)
        cur = 0

cur = 0
for i in range(2, len(s)-1, 3):
    if s[i:i+3] == 'EBA':
        cur += 3
        mx = max(mx, cur)
    else:
        if s[i:i+2] == 'EB':
            mx = max(mx, cur + 2)
        elif s[i+1] == 'E':
            mx = max(mx, cur + 1)
        cur = 0

        
print(mx)