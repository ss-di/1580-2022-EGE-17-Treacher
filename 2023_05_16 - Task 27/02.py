n = int(input())

data = [int(input()) for i in range(n)]

mx = 0
for i in range(n):
    for j in range(i+6, n):
        if (data[i] * data[j]) %2 != 0:
            mx = max(mx, data[i] * data[j])
        
print(mx)