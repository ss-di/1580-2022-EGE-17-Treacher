with open('26.txt') as f:
    data = f.readlines()
print(data)
max_vol, n = map(int, data[0].split())
del data[0]
print(max_vol, n, data)
data = list(map(int, data))
print(max_vol, n, data)
data.sort()
print(max_vol, n, data)
cnt = 0
vol = 0

for x in data:
    if vol + x <= max_vol:
        cnt += 1
        vol += x
        last_size = x
print(cnt, vol)
ost = max_vol - vol
max_file_size = last_size + ost

for x in data:
    if x <= max_file_size:
        otv2 = x
print(otv2)