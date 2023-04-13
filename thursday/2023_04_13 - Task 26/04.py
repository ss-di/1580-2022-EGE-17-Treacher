#https://inf-ege.sdamgia.ru/problem?id=40741

def get_dels(x):
    dels = []
    d = 1
    while d*d < x:
        if x % d == 0:
            dels.append(d)
            dels.append(x // d)
        d += 1
    if x % d == 0:
        dels.append(d)
    dels.sort()
    return dels


def ok(x):
    dels = get_dels(x)
    if len(dels) < 3:
        return 0
    if dels[-2] + dels[-3] < 10000:
        return dels[-2] + dels[-3]
    else:
        return 0

X = 10_000_000
print(X**0.5)
cnt = 0
while cnt < 5:
    sd = ok(X)
    if sd:
        print(X, sd)
        cnt += 1
    X += 1