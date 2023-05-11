fn = '270_7603.txt'
fn = '27A_7603.txt'
#fn = '27B_7603.txt'

with open(fn) as f:
    data = f.readlines()
    
print(data[:3], data[-3:])

data = list(map(int, data))
print(data[:3], data[-3:])

#print(data)
n = data[0]
k = data[1]
del data[0]
del data[0]
#print(data)

print(n, k, data[:3], data[-3:])

mx = -1
for i in range(n-2*k):
    for j in range(i+k, n-k):
        s = sum(data[i:i+k]) + sum(data[j:j+k])
        if s % 68 == 0:
            mx = max(mx, s)

print(mx)
