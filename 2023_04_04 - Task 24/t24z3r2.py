s = open('24-153.txt').readline()

print(s[-2:])
s = s[:-1] # убираем символ перевода строки

mx = 0

for st in range(len('EAB')):
    cur = 0
    for i in range(st, len(s), 3):
        if s[i:i+3] == 'EAB':
            cur += 1
            mx = max(mx, cur)
        else:
            if s[i] == 'E':
                mx = max(mx, cur+1)
            cur = 0
        p = s[i]

print(mx)
