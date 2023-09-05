def hod(x, to):
    if x == 20:
        return 0
    if x == to:
        return 1
    if x > to:
        return 0
    return hod(x+1, to) + hod(x+2, to) + hod(x*3, to)

print(hod(4, 10) * hod(10, 22))