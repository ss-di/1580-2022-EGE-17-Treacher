f = []
for i in range(4):
    f.append(i)
print(f)

for n in range(4, 101):
    if n % 3 == 0:
        f.append(n**3 + f[-1])
    elif n % 3 == 1:
        f.append(4 + f[n//3])
    else:
        f.append(n**2 + f[n-2])
        
print(f[-1])
