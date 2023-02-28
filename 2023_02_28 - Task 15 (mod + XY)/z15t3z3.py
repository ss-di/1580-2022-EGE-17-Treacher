for N in range(1, 1000):
    cnt = 0
    for x in range(-5, 100):
        F = ((not (70 <= x <= 90)) <= (40 <= x <= 60)) and ((not (0 <= x <= N)) <= (70 <= x <= 90))
        if F:
            cnt += 1
    if cnt > 30:
        print(N)
        break
