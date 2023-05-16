n = int(input())

data = [int(input()) for i in range(n)]

mn3c = 1000*1000 + 1
mn_any_c = 1000*1000 + 1

mn3n = 1000*1000 + 1
mn_any_n = 1000*1000 + 1

mn = 1000*1000 + 1

for i in range(20, n):
    if data[i-20] % 2 == 0:
        mn_any_c = min(mn_any_c, data[i-20])
    else:
        mn_any_n = min(mn_any_n, data[i-20])
    if data[i-20] % 3 == 0:
        if data[i-20] % 2 == 0:
            mn3c = min(mn3c, data[i-20])
        else:
            mn3n = min(mn3n, data[i-20])

    if data[i] % 2 == 0:
        mn = min(mn, mn3n * data[i])
        if data[i] % 3 == 0:
            mn = min(mn, mn_any_n * data[i])
    else:
        mn = min(mn, mn3c * data[i])
        if data[i] % 3 == 0:
            mn = min(mn, mn_any_c * data[i])

if mn == 1000*1000 + 1:
    mn = -1
print(mn)