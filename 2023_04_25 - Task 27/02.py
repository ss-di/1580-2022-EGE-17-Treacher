with open('00.txt') as f:
    data = f.readlines()

data = list(map(int, data))

# n = int(input())
# data = [int(input()) for i in range(n)]

n = data[0]
del data[0]
print(n, data[:3], data[-3:])

INF = 1000000
ans = -1
buf = data[:3]
mins = [-1] * 10
for x in data[3:]:
    a = buf[0]
    mins[a % 10] = max(mins[a % 10], a)
    del buf[0]
    buf.append(x)
    for i in range(10):
        s = x + mins[i]
        if s % 10 == 7 and s > ans:
            ans = s
            
if ans == INF:
    ans = -1
print(ans)