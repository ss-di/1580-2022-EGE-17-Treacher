with open('24.txt') as f:
    s = f.read()


s = s.replace('\n', '')
prev = '*'
mx = 0
cur = 0
for i in range(len(s)):
    if s[i] == 'E' and (prev == 'F' or cur == 0) or \
       s[i] == 'F' and (prev == 'E' or cur == 0):
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0
    prev = s[i]
print(mx)

s = s.replace('D', '*').replace('EE', 'E*E').replace('FF', 'F*F')
s = s.split('*')
print(max(map(len, s)))
