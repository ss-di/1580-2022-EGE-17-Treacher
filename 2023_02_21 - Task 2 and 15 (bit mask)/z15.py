def f( x, a ):
    return (x & 125 != 1) or ((x & 34 == 2) <= (x & a == 0))


for a in range(1, 1000):
    for x in range(1,1000):
        if not f(x, a):
            break
    else:
        print( a )
        break
