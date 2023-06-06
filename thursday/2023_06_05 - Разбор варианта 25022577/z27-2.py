print(1*2 + 3*1 + 5*1 + 6*1 + 8*2)
fn = "27_0_7097.txt"; k = 96
fn = "27_A_7097.txt"; k = 44
fn = "27_B_7097.txt"; k = 44

with open(fn) as f:
    data = f.readlines()
    
print(data[:3], data[-3:])

n = int(data[0])
del data[0]

pkont = [0]
kont = [0] * n
rast = [0] * n
for i in range(n):
    data[i] = list(map(int, data[i].split()))
    kont[i] = (data[i][1] + k-1) // k
    rast[i] = data[i][0]
    pkont.append(pkont[-1] + kont[i])
print(n, data[:3], data[-3:])

#print(rast)
#print(kont)
#print(pkont)

s = 0
for j in range(n):
    s += abs(rast[0] - data[j][0]) * kont[j]
allk = sum(kont)
mn = s
#print(s)
for i in range(1, n):
    s += pkont[i] * (rast[i] - rast[i-1])
#    print(s)
    s -= (allk - pkont[i]) * (rast[i] - rast[i-1])
#    print(i, s)
    mn = min(mn, s)
print(mn)