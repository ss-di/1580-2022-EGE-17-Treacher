with open('27_B.txt') as f:
    data = f.readlines()
    
print(data[:3])
n = int(data[0])
del data[0]
print(n, len(data))

s = 0
razn = []
for i in data:
    a, b = map(int, i.split())
    s += max(a, b)
    if abs(a-b) % 13 != 0:
        razn.append(abs(a-b))
    
print(s, s % 13)
razn.sort()
print(razn[:10])
s = s-min(razn)
print(s, s % 13)