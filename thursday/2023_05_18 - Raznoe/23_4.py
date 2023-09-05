def calc(x, l):
    if len(l) == 13:
        if x < 0: # and l[-2]=="1":
            return {x}
        else:
            return set()
    else:
        return calc(x-3, l+"1").union(calc(x*(-3), l+"2"))


ans = calc(333, "")
print(len(ans))