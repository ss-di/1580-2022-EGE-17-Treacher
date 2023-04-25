#fn = '27-r01.txt'
fn = '4-a.txt'
fn = '4-b.txt'
with open(fn) as f:
    data = f.readlines()

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = list(map(int, data[i].split()))
print(n, data[:3], data[-3:])

# for i in range(n):
#     a = data[i][0]
#     b = data[i][1]

k = 3
s = 0
diff = []
for a, b in data:
    s += min(a, b)
    r = abs(a - b)
    if r % k != 0:
        diff.append(r)
    
diff.sort()
print(s, s % k)
print(s+317, (s+317) % k)
#for i in range(len(diff)):
#    print(diff[i], diff[i] % k)

INF = s+1
ans = [INF] * k
ans[0] = 0

for d in diff:
    ans2 = ans.copy()
    for i in range(k):
        ans2[(i + d) % k] = min(ans[(i + d) % k], ans[i] + d)
    ans = ans2
    
s = s + ans[(k - s % k) % k]
print(s, s % k)
'''
[1, 1, 2, 4]
'''