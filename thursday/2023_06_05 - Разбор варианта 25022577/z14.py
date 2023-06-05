def to25(x):
    bukv = "QWERTYUIOPASDFGHJKLZXCVBNM"
    bukv =  sorted(bukv)
    bukv = ''.join(bukv)
    digs = "0123456789" + bukv
    print(digs)
    x6 = ""
    while x:
        x6 = digs[x % 25] + x6
        x = x // 25
    return x6

n = 3 * 625**173 + 4 * 125**180 + 3 * 25**157 + 2 * 5 ** 155 + 156
n25 = to25(n)
print(n25.count("0"))