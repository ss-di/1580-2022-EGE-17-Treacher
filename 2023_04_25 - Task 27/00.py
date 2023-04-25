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
for i in range(n):
    for j in range(i+3, n):
        s = data[i] + data[j]
        if s < ans and s % 10 == 4:
            ans = s
            
if ans == INF:
    ans = -1
print(ans)