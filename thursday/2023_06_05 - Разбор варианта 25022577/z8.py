def to6(x):
    digs = "0123456789ABCDEFGH"
    x6 = ""
    while x:
        x6 = digs[x % 6] + x6
        x = x // 6
    return x6

a = 6 ** 5
print(to6(a))
b = 6 ** 6 - 1
print(to6(b))

cnt = 0
for x in range(a, b + 1):
    x6 = to6(x)
    if x6.count("2") != 1:
        continue
    x6 = "0" + x6 + "0"
    p2 = x6.find("2")
    if int(x6[p2-1]) % 2 == 0 and int(x6[p2+1]) % 2== 0:
        cnt += 1
        print(x6)

print(cnt)