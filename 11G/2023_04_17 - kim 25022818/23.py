def calc(f, t):
    if f == t:
        return 1
    if f > t:
        return 0
    if f == 26:
        return 0
    return calc(f+1, t) + calc(f*2, t)

print(calc(2, 11) * calc(11, 39))
