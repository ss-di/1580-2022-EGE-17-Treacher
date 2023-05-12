with open('26-84.txt') as f:
    n = int(f.readline())
    gr = list(map(int, f.readline().split()))
    aud = list(map(int, f.readline().split()))
    
print(n)
gr.sort()
aud.sort()
print(gr[:5], gr[-5:])
print(aud[:5], aud[-5:])

cnt = 0
for x in gr:
    if x <= aud[0]:
        cnt += 1
    else:
        break
print('2:', cnt)

kols = [0] * n
j = 0
for i in range(n):
    if i > 0:
        kols[i] = kols[i-1]
    while j < n and gr[j] <= aud[i]:
        kols[i] += 1
        j += 1

print(kols[:5], kols[-5:])

ans = 1
for i in range(n):
    ans *= kols[i] - i
    ans %= 100000007
print(ans)