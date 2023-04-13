#data = open('26.txt').readlines()

#with open('26.txt') as f:
#    data = f.readlines()

f = open('26.txt') 
data = f.readlines()
f.close()


print(data)
#max_vol, n = data[0].split()
#max_vol = int(max_vol)
#n = int(n)

max_vol, n = list(map(int, data[0].split()))
print(max_vol, n)

del data[0]

data = list(map(int, data))
print(data)

data.sort()
print(data)

cnt = 0
s = 0
for i in range(n):
    if s + data[i] <= max_vol:
        s += data[i]
        cnt += 1
        last = data[i]
    else:
        break
print(cnt)
max_file = last + max_vol-s
print(max_file)

ans2 = data[0]
for i in range(n):
    if data[i] <= max_file and data[i] > ans2:
        ans2 = data[i]
print(ans2)