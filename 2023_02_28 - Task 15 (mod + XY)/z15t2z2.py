for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (y + 3*x < A) or (2*y + x > 50) or (4*y - x < 40)
            if not F:
                ok = False
    if ok:
        print(A)
        break
