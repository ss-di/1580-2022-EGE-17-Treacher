print ('x', 'y', 'z', 'w')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = not (x == (y <= z))
            print(x, y, z, int(F))
'''
x y z w
0 0 1 1
1 0 1 0

0 1 0 0
0 1 1 1
1 0 0 0
1 1 0 1
'''