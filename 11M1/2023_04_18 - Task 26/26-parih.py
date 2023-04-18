with open('26-parih.txt') as f:
    data = f.readlines()
    
k = int(data[0])
n = int (data[1])
del data[0]
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))

zan = [[0]*601 for i in range(k)]

'''
1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 0 0 0
0 0 0 0 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0

3 7
5 10
1 2
'''

cnt = 0
for i in range(n):
    f, t = data[i]
    for sp in range(k):
        if zan[sp][f: t+1].count(1) == 0:
            zan[sp][f: t+1] = [1]*(t-f+1)
            data[i].append(sp)
            cnt += 1
            break
    else:
        data[i].append(-1)

print(*data, sep='\n')

print(cnt)

