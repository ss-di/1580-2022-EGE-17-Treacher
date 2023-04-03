s = open('24.txt').readline()

print(s[-2:])
s = s[:-1] # убираем символ перевода строки

cur = mx =  0
for i in range(len(s)):
    if s[i] == 'Z':
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0

print(mx)
