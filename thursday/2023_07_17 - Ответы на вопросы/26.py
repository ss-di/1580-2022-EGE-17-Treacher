with open("26.txt") as f:
    data = f.readlines()

print(data[:2], data[-2:])

m, k, n = map(int, data[0].split())
del data[0]
print(m, k, n, len(data), data[:2], data[-2:])

for i in range(n):
    data[i] = list(map(int, data[i].split()))
print(m, k, n, len(data), data[:2], data[-2:])

cur = []
cnt_full = 0
cnt_pass = 0
for g in range(1, m+1):
    cur2 = []
    for i in range(len(cur)):
        if cur[i] != g:
            cur2.append(cur[i])
    cur = cur2
    pret = []
    for i in range(n):
        if data[i][0] == g:
            pret.append(data[i][1])
    pret.sort(reverse=True)
    for i in range(min(len(pret), k-len(cur))):
        cur.append(pret[i])
        cnt_pass += 1
    if len(cur) == k:
        cnt_full += 1
print(cnt_pass, cnt_full)