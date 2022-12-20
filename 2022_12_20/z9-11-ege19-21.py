def hod(a, mh, h):
    if a <= 12:
        if h%2==1:
            return 1
        else:
            return 2
    h += 1
    if h > mh:
        return 3
    res = []
    res.append(hod(a - 1, mh, h))
    if a%2==0: res.append(hod(a // 2, mh, h))

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

for s in range(13, 100):
    print(s, end='\t')
    for g in range(1, 6):
        print(hod(s, g, 0), end='\t')
    print()
