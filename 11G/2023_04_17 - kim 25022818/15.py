def check(A):
    for x in range(10000):
        for y in range(10000):
            F = (x < A) or (y < A) or (x + 2*y > 150)
            if not F:
                return False
    return True

for A in range(100000000):
    if check(A):
        print(A)
        break