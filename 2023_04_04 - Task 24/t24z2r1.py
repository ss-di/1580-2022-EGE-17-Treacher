s = open('24.txt').readline()

print(s[-2:])
s = s[:-1] # убираем символ перевода строки

cur = mx = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1

print(mx)
