s = open('24-153.txt').readline()

print(s[-2:])
s = s[:-1] # убираем символ перевода строки

cur = mx = 0
p = '*'
for i in range(len(s)):
    if p != 'E' and s[i] == 'E' or \
       p == 'E' and s[i] == 'A' or \
       p == 'A' and s[i] == 'B':
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1
    p = s[i]

print(mx, (mx+2)//3)
