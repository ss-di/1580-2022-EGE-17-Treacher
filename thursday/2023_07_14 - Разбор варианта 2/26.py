with open("26.txt") as f:
    data = f.readlines()
    
print(data[:2], data[-2:])
for i in range(len(data)):
    data[i] = list(map(int, data[i].split()))
    data[i] += [0]
print(data[:2], data[-2:])

t, n, mx, tmp = data[0]
del data[0]
print(t, n, mx, len(data))

mx_t = data[0][1]
for i in range(len(data)):
    mx_t = max(mx_t, data[i][1])

for cur_t in range(t, mx_t+1):
    if cur_t % t == 0:
        tov = 1
    if tov:
        p = -1
        for i in range(n):
            if not(data[i][0] <= cur_t <= data[i][1]): continue
            if data[i][2] >= mx: continue
            if p == -1:
                p = i
            else:
                if data[i][2] < data[p][2] or \
                   data[i][2] == data[p][2] and data[i][1] > data[p][1]:
                    p = i
        if p != -1:
            data[p][2] += 1
            data[p][3] += 1
            tov = 0

data.sort(key=lambda x:x[3], reverse=True)
print(data[:3])
print(data[0][1]-data[0][0]+1, data[0][3])
