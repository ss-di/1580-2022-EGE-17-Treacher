def calc(f, t):
    if t < f:
        return 0
    if f == t:
        return 1
    if t % 4 == 0:
        return calc(f, t - 1) + calc(f, t // 4)
    else:
        return calc(f, t - 1)

print(calc(1, 55))