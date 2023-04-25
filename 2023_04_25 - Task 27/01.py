with open('00.txt') as f:
    data = f.readlines()

data = list(map(int, data))

# n = int(input())
# data = [int(input()) for i in range(n)]

n = data[0]
del data[0]
print(n, data[:3], data[-3:])

INF = 1000000
ans = INF
buf = data[:3]
mins = [INF] * 10
for x in data[3:]:
    a = buf[0]
    mins[a % 10] = min(mins[a % 10], a)
    del buf[0]
    buf.append(x)
    for i in range(10):
        s = x + mins[i]
        if s % 10 == 4 and s < ans:
            ans = s
            
if ans == INF:
    ans = -1
print(ans)