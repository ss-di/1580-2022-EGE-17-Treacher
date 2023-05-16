n = int(input())

data = [int(input()) for i in range(n)]


mn1 = 1000*1000 + 1
mn = 1000*1000 + 1

for i in range(6, n):
    if data[i-6] % 2 != 0:
        mn1 = min(mn1, data[i-6])
    if data[i] % 2 != 0:
        mn = min(mn, mn1 * data[i])

if mn == 1000*1000 + 1:
    mn = -1
print(mn)