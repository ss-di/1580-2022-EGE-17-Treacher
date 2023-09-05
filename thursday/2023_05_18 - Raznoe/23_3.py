def calc(x, l):
    global ans
    if len(l) == 13:
        if x < 0: # and l[-2]=="1":
            ans.add(x)

    else:
        calc(x-3, l+"1")
        calc(x*(-3), l+"2")

ans = set()

calc(333, "")
print(len(ans))