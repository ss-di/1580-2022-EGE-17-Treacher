v = []
for x in range(100):
    for y in range(100):
        for z in range(100):
            k2 = 2*x+3*y+6*z
            k3 = y+z
            if k2 == 186 and k3 == 26:
                print(x, y, z)
                v.append((x+y+z, x, y, z))

print(min(v))