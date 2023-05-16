n = int(input())

data = [int(input()) for i in range(n)]


mn = 1000*1000 + 1
for i in range(n):
    for j in range(i+6, n):
        if (data[i] * data[j]) %2 != 0:
            mn = min(mn, data[i] * data[j])
        
if mn == 1000*1000 + 1:
    mn = -1
print(mn)