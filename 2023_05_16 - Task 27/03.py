n = int(input())

data = [int(input()) for i in range(n)]

mx1 = 0
mx = 0

for i in range(8, n):
    if data[i-8] % 2 != 0:
        mx1 = max(mx1, data[i-8])
    if data[i] % 2 != 0:
        mx = max(mx, mx1 * data[i])

print(mx)