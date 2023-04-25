fn = '27-r01.txt'
#fn = '3-a.txt'
#fn = '3-b.txt'
with open(fn) as f:
    data = f.readlines()

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))
del data[-1]
print(n, data[:3], data[-3:])

# for i in range(n):
#     a = data[i][0]
#     b = data[i][1]

s = 0
diff = []
for a, b in data:
    s += max(a, b)
    r = abs(a - b)
    if r % 6 != 0:
        diff.append(r)
    
diff.sort()
print(s, s % 6)
print(diff)

'''
[1, 1, 2, 4]
'''