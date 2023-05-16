n = int(input())

data = [int(input()) for i in range(n)]


cnt = 0
for i in range(n):
    for j in range(i+7, n):
        if (data[i] + data[j]) % 6 == 0:
            cnt += 1
        
print(cnt)