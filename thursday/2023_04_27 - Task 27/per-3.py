fn = '27-75.txt'
fn = '27-45788A.txt'

with open(fn) as f:
    data = f.readlines()
    
data = list(map(int, data))

n = data[0]
del data[0]

print(n, data[:2], data[-2:])

cnt = 0
for i in range(n):
    for j in range(i+17, n):
        for k in range(j+17, n):
            s = data[i] + data[j] + data[k]
            if s % 7717 == 0:
                cnt += 1
                
print(cnt)