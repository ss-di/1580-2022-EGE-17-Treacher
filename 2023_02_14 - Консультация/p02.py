def avt(x):
    x3 = ''
    while x:
        x3 = str(x % 3) + x3
        x = x // 3
    x3 += x3[-1]
    return int(x3, 3)

m = []
for i in range(1, 10000): 
    if avt(i) >= 1000:
        m.append(avt(i))
        print(i, m[-1])
    
print(min(m))