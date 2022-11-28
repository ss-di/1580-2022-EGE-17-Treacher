def hod(a, mh, h=0, ph=0):
    if a >= 43:
        if h % 2 == 1:
            return 1
        else:
            return 2
    
    h += 1
    if h > mh:
        return 3

    res = []
    if ph!=1: res.append(hod(a + 1, mh, h, 1))
    if ph!=2: res.append(hod(a + 2, mh, h, 2))
    if ph!=3: res.append(hod(a * 2, mh, h, 3))
    
    if h % 2 == 1:
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

print(' ', end='\t')
for mh in range(1, 6):
    print(mh, end='\t')
print()

for a in range(1, 28+1):
    print(a, end='\t')
    for mh in range(1, 6):
        print(hod(a, mh), end='\t')
    print()
