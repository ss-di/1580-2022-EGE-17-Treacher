for A in range(1, 1000):
    for x in range(1, 1000):
        F = (not (x % A == 0)) <= ((x % 6 == 0) <= (not (x % 9 == 0)))
        if not F:
            break
    else:
        print(A)