with open('39247.txt') as f:
    data = f.readlines()

print(data[:3], data[-3:])
data = list(map(int, data))
print(data[:3], data[-3:])
n = data[0]
del data[0]
print(n, data[:3], data[-3:])

data.sort()
print(n, data[:3], data[-3:])

posl = []

for i in range(n):
    p = len(posl) + 1
    if data[i] % p == 0:
        posl.append(data[i])

print(posl)
print(len(posl))

for i in range(n-1, 0, -1):
    if data[i] % len(posl) == 0:
        print(len(posl), data[i])
        break