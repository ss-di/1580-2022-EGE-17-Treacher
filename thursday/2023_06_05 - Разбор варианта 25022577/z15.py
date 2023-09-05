for A in range(1, 1000):
    for x in range(1, 1000):
        F = (x % A == 0) or ((50 <= x <= 70) <= (x % 16 != 0))
        if not F:
            break
    else:
        print(A)
