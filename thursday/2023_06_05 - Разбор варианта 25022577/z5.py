print ("X Y W Z")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = (not (y <= w)) or (x <= z) or (not x)
                if not F:
                    print(x, y, z, w)