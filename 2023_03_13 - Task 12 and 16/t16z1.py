f = []
for i in range(6):
    f.append(i+15)
print(f)

for n in range(6, 1001):
    if n % 2 == 0:
        f.append(f[n // 2] + n**3 - 1)
    else:
        f.append(f[n-1] + 2*n**2 + 1)
        
print(f[:10])
cnt = 0
for x in f:
    if str(x).count('8') >= 2:
        cnt += 1
print(cnt)