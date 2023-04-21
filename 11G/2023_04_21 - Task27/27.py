with open('28133_B.txt') as f:
    data = f.readlines()
    
n = int(data[0])
del data[0]
data = list(map(int, data))

print(n, data)

k = 120

mx = -1
big = [-1] * k
for x in data:
    para = big[(k - x % k) % k]
    if para != -1 and para > x:
        mx = max(mx, para+x)
        print(x, para, (x+para) % k)
    big[x % k] = max(big[x % k], x)

print(mx)
    