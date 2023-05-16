fn = "270_7881.txt"
fn = "27A_7881.txt"
fn = "27B_7881.txt"

with open(fn) as f:
    data = f.readlines()

print(data[:3], data[-3:])

data = list(map(int, data))
n = data[0]
k = data[1]
del data[0]
del data[0]
print(n, k, data[:3], data[-3:])

ost3c = [0] * 100
ost3n = [0] * 100

cnt = 0
for i in range(n):
    x = data[i]
    if x % 37 == 0:
        cnt += ost3n[x % 100]
        ost3c[x % 100] += 1
    else:
        cnt += ost3c[x % 100]
        ost3n[x % 100] += 1
    if i >= k:
        if data[i-k] % 37 == 0:
            ost3c[data[i-k] % 100] -= 1
        else:
            ost3n[data[i-k] % 100] -= 1
        
print(cnt)

#0 - 5
#A - 73
#B - 1146648