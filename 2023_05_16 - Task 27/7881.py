fn = "270_7881.txt"
fn = "27A_7881.txt"
#fn = "27B_7881.txt"

with open(fn) as f:
    data = f.readlines()

print(data[:3], data[-3:])

data = list(map(int, data))
n = data[0]
k = data[1]
del data[0]
del data[0]
print(n, k, data[:3], data[-3:])

cnt = 0
for i in range(n):
    for j in range(i+1, min(i+k+1, n)):
        if (data[i] - data[j]) % 100 == 0 and (data[i] % 37 == 0) != (data[j] % 37 == 0):
            cnt += 1

print(cnt)

#0 - 5
#A - 73
#B - 