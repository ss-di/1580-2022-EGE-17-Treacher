def calc(f, t):
    if f > t:
        return 0
    if f == t:
        return 1
    return calc(f + 1, t) + calc(f * 4, t)

print(calc(1, 55))