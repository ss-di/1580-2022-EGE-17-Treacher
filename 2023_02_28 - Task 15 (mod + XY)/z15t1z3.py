def D(x, y):
    return x % y == 0

for A in range(1, 1000):
    for x in range(1, 1000):
        F = ((not D(x, A)) and D(x, 15) ) <= ((not D(x, 18)) or (not D(x, 15)))
        if not F:
            break
    else:
        print(A)