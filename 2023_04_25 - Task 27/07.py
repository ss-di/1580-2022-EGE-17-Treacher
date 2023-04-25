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

k = 6
s = 0
diff = []
for a, b in data:
    s += max(a, b)
    r = abs(a - b)
    if r % k != 0:
        diff.append(r)
    
diff.sort()
print(s, s % k)
print(diff)
INF = s+1
ans = [INF] * k
ans[0] = 0

for d in diff:
    ans2 = ans.copy()
    for i in range(k):
        ans2[(i + d) % k] = min(ans[(i + d) % k], ans[i] + d)
    ans = ans2
    print(ans)
    
s = s - ans[s % k]
print(s, s % k)
'''
[1, 1, 2, 4]
'''