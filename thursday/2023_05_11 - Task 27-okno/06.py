fn = '270_7603.txt'
fn = '27A_7603.txt'
fn = '27B_7603.txt'

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

prev_mx = -1
mx = -1
for i in range(k, n):
    prev_mx = max(prev_mx, data[i - k])
    mx = max(mx, prev_mx + data[i])

print(mx)
