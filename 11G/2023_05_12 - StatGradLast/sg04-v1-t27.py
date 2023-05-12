with open('27-0.txt') as f:
    data = f.readlines()
    
data = list(map(int, data))
n = int(data[0])
del data[0]

print(n, data[:3], data[-3:])

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if (j-i) % 9 == (data[i] + data[j]) % 9:
            print(data[i], data[j])
            cnt += 1
print(cnt)

# A 346204
