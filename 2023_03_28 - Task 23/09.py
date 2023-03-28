def calc(f, t):
    if f > t:
        return 0
    if f == t:
        return 1
    return calc(f + 1, t) + calc(f * 2, t) + calc(f * 3, t)

print(calc(1, 16) * calc(16, 22))