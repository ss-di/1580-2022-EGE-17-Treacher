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

mx21 = -1
mx3 = -1
mx7 = -1
mx = -1
for i in range(n):
    if data[i] % 21 == 0 and data[i] > mx21:
        mx = max(mx, mx21)
        mx21 = data[i]
    elif data[i] > mx:
        mx = data[i]

    if data[i] % 3 == 0 and data[i] % 7 != 0:
        mx3 = max(mx3, data[i])
    if data[i] % 3 != 0 and data[i] % 7 == 0:
        mx7 = max(mx7, data[i])


print(mx, mx21, mx3, mx7)
print(max(mx*mx21, mx3*mx7))
