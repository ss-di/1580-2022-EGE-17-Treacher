fn = '270_7603_1.txt'
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

mx1 = -1
mx2 = -1
for i in range(n):
    if data[i] > mx1:
        mx2 = mx1
        mx1 = data[i]
    elif data[i] > mx2:
        mx2 = data[i]

print(mx1+mx2, mx1, mx2)
