def is_prime(x):
    if x == 1:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def get_dels(x):
    ans = []
    d = 1
    while d*d < x:
        if x % d == 0:
            ans.append(d)
            ans.append(x // d)
        d += 1
    if d * d == x:
        ans.append(d)
    ans.sort()
    return ans


A = 77_777_777
B = 88_888_888

for x in range(A, B+1):
    tmp = x
    while x % 2 == 0:
        x //= 2
    x4 = round(x**0.25)
    if x4**4 == x and is_prime(x4):
        dels = get_dels(x)
        print(tmp, dels[1])