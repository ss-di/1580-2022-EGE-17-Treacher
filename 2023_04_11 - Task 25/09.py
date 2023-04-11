#012345678
#1?34567?9

for x in range(17, 10**9 + 1, 17):
    xs = str(x)
    if xs[0] == '1' and \
       xs[2:2+5] == '34567' and \
       xs[-1] == '9' and len(xs)==9:
        print(x, x // 17)