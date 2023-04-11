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

x = 1
ans = []
while x**4 <= B:
    if is_prime(x):
        tmp = x**4
        while tmp <= B:
            if tmp >= A:
                ans.append((tmp, x))
            tmp *= 2
    x += 1
ans.sort()
print(*ans, sep='\n')