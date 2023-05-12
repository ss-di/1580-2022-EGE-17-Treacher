with open('27-B.txt') as f:
    data = f.readlines()
    
data = list(map(int, data))
n = int(data[0])
del data[0]

print(n, data[:3], data[-3:])

m = [[0] * 9 for i in range(9)]

cnt = 0
for i in range(n): #i = 30
    x = data[i]
    for r in range(9):
        cnt += m[(i-r) % 9][(r-x%9) % 9] # (x+y)%9=r

    m[i % 9][x % 9] += 1
#    print(i)
#    print(*m, sep='\n')
    

print(cnt)

# A 346204
# B 620548 407867