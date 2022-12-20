def hod(a, b, mh, h):
    if a == 0 or b == 0 or ((a<3 or b<3) and (a%2==1 and b%2==1)):
        if h%2==1:
            return 1
        else:
            return 2
    h += 1
    if h > mh:
        return 3
    res = []
    if a>=3 and b>=3: res.append(hod(a - 3, b - 3, mh, h))
    if a%2==0: res.append(hod(a // 2, a // 2, mh, h))
    if b%2==0: res.append(hod(b // 2, b // 2, mh, h))

    if h%2==1:
        if 1 in res:
            return 1
        elif 3 in res:
            return 3
        else:
            return 2
    else:
        if 2 in res:
            return 2
        elif 3 in res:
            return 3
        else:
            return 1


print(end='\t')
for i in range(1, 6):
    print(i, end='\t')
print()

N = 20
for K in range(1, 200):
    print(K, end='\t')
    for g in range(1, 6):
        print(hod(N, K, g, 0), end='\t')
    print()
