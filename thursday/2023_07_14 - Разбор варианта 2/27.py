fn = "270.txt"
fn = "27A.txt"
# fn = "27B.txt"

with open(fn) as f:
    data = f.readlines()
    
print(data[:2], data[-2:])
data = list(map(int, data))
print(data[:2], data[-2:])
n = data[0]
del data[0]
k = data[0]
del data[0]
print(n, len(data), k, data[:2], data[-2:])

mx = 0
for i in range(n-k):
    for j in range(i+k, n):
        if data[i] + data[j] > mx:
            mx = data[i] + data[j]
            a = i
            b = j
        elif data[i] + data[j] == mx:
            if j-i > b-a:
                a = i
                b = j
                
print(b-a, mx)