for A in range(1, 1000):
    ok = True
    for x1 in range(400, 600):
        x = x1 / 100
        for y1 in range(400, 600):
            y = y1 / 100
            F = (x*y < A) or (x < y) or ( 5 <= x)
            if not F:
                ok = False
    if ok:
        print(A)
        break
