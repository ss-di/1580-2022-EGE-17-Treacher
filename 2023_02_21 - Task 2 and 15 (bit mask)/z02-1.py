print('x', 'y', 'z', 'w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))
                if F == 0:
                    print(x, y, z, w)
                    