def calc(ans, x, l):
    if l == 13:
        if x < 0:
            ans.add(x)

    else:
        calc(ans, x-3, l+1)
        calc(ans, x*(-3), l+1)

ans = set()

calc(ans, 333, 0)
print(len(ans))