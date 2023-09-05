fn = "270.txt"
fn = "27A.txt"
fn = "27B.txt"

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

mx1 = mx = 0

for i in range(k, n):
    if data[i-k] > mx1:
        mx1 = data[i-k]
        a1 = i-k
    if data[i] + mx1 > mx or \
       data[i] + mx1 == mx and i-a1 > b-a:
        mx = data[i] + mx1
        a = a1
        b = i
print(b-a, mx)


#0 = 3 45
#A = 284 174902
#B = 3224855 3094684
#B = 3224855 3094684