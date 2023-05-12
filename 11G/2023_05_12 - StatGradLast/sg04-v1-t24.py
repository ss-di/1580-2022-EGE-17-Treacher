with open('24.txt') as f:
    data = f.readlines()
    
print(len(data))

s = data[0]

print(s[:3], s[-3:], "*")

r = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

p = 0
cur = mx = 0
for i in range(len(s)):
    if s[i:i+3] in r:
        p = 2
        cur = 0
    elif p > 0:
        p -= 1
    else:
        cur += 1
        mx = max(mx, cur)
    
print(mx)