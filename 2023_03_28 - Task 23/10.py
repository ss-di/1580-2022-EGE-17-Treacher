def calc(f, t):
    if f == 25:
        return 0
    if f > t:
        return 0
    if f == t:
        return 1
    return calc(f + 1, t) + calc(f * 2, t)

print(calc(2, 14) * calc(14, 29))