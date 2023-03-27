def calc(f, t):
    if t < f:
        return 0
    if t == f:
        return 1
    if t % 3 == 0:
        return calc(f, t - 1) + calc(f, t // 3)
    return calc(f, t - 1)


print(calc(1, 20))
