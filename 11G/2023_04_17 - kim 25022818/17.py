with open('17.txt') as f:
    data = f.readlines()
    
data = list(map(int, data))

print(data[:10])

mx12 = 0
for x in data:
    if x % 100 == 12 and x > mx12:
        mx12 = x
print(mx12)

mx12 = 0
for x in data:
    if str(x)[-2:] == '12' and x > mx12:
        mx12 = x
print(mx12)

cnt = 0
mx = 0
for i in range(1, len(data)):
    if (str(data[i])[-2:] == '12') != (str(data[i-1])[-2:] == '12') and \
       (data[i] + data[i-1]) ** 2 < mx12 ** 2:
        cnt += 1
        mx = max(mx, data[i] + data[i-1])
print(cnt, mx)