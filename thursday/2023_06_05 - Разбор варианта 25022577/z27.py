print(1*2 + 3*1 + 5*1 + 6*1 + 8*2)
fn = "27_0_7097.txt"; k = 96
fn = "27_A_7097.txt"; k = 44
#fn = "27_B_7097.txt"; k = 44

with open(fn) as f:
    data = f.readlines()
    
print(data[:3], data[-3:])

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))
    
print(n, data[:3], data[-3:])

mn = 10**10000
for i in range(n):
    p = data[i][0]
    s = 0
    for j in range(n):
        s += abs(p - data[j][0]) * ((data[j][1] + k-1) // k)
    mn = min(mn, s)
print(mn)