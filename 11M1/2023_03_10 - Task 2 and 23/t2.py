print ('x', 'y', 'z', 'w')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == y) <= (z == w)
                if not F:
                    print(x, y, z, w)
'''
x y z W
0 0 0 1
1 1 1 0

x y Z w
0 0 1 0
1 1 0 1

'''