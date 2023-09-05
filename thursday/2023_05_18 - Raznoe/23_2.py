def calc(x, l):
    global ans
    if l == 13:
        if x < 0:
            ans.add(x)

    else:
        calc(x-3, l+1)
        calc(x*(-3), l+1)

ans = set()

calc(333, 0)
print(len(ans))