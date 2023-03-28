def calc(f, t, l=0):
    if f > t:
        return 0
    if f == t:
        return 1
    l += 1
    if l > 5:
        return 0
    return calc(f + 1, t, l) + calc(f * 2, t, l) + calc(f + f % 4, t, l)

cnt = 0
for i in range(-10, 80+1):
    if calc(i, 80) > 0:
        cnt += 1
print(cnt)