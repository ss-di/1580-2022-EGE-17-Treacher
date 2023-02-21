def f( x, a ):
    return ((x&28!=0) or (x&45!=0)) <= ((x&17==0) <= (x&a!=0))


for a in range(0, 1000):
    for x in range(0, 1000):
        if not f(x, a):
            break
    else:
        print( a )
        break
