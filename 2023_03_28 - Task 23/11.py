def calc(f, t):
    if f in  [10, 11]:
        return 0
    if f > t:
        return 0
    if f == t:
        return 1
    return calc(f + 1, t) + calc(f + 2, t) + calc(f * 3, t)

print(calc(1, 8) * calc(8, 28))