with open('26-101.txt') as f:
    data = f.readlines()
#print(data)

n, k = map(int, data[0].split())
del data[0]
#print(n, k, data)

for i in range(n):
    data[i] = int(data[i])
print(n, k, data)

data.sort()

stop = 0
mx_cnt = 0
while data:
    stop += 1
    cnt = 1
    last = data[0]
    del data[0]
    data2 = []
    for x in data:
        if x >= last + k:
            cnt += 1
            last = x
        else:
            data2.append(x)
    data = data2
    mx_cnt = max(mx_cnt, cnt)
    
print(mx_cnt, stop)